from project import app, db
from project.models import User, Admin,Progress_comment,Progress_report, Proposal,Previous_topic,Department,Project,Rejected_Proposal,Partner_table
from flask_restful import Resource, Api
from flask import flash, redirect, render_template, request, url_for,make_response
from flask_login import login_user,login_required, logout_user
from .forms import LoginForm,RegisterForm,Proposal_submittion_Form
from project.models import User
from project import db, login_manager,mail
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash,check_password_hash
import os
import functools
from flask_login import login_user,login_required,logout_user
import json
import logging
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash,check_password_hash
import jwt
from functools import wraps
import datetime
from flask_mail import Message

api = Api(app)

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return make_response('Invalid Token',401,{'www-Authenticate':'Invalid Token"'})
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
            current_user = User.query.filter_by(reg_no=data['reg_no']).first()
        except:
            return make_response('Invalid Token',401,{'www-Authenticate':'Invalid Token"'})
        return f(current_user,*args,**kwargs)   
    return decorated


class Register(Resource):
    
    #@staticmethod
    def post(self):
        '''Generating public ID'''
        publicID = str(uuid.uuid4())
        data = request.get_json()
        
        student1 = data['student1']
        reg_no = data['reg_no']
        email = data['email']
        tel = data['tel']
        course = data['course']
        password = data['password']
        confirm_password = data['confirm_password']

        #form = RegisterForm()
        #try:
        #    reg_no,email, password = request.json.get('reg_no').strip(), request.json.get('email').strip(),request.json.get('password').strip()
        #except Exception as why:
            # Log input strip or etc. errors.
        #    logging.info("Username, password or email is wrong. " + str(why))
        #    flash('status:invalid input')
        if reg_no is None or password is None :
            return {'error':'error'}

        if password==confirm_password:
            
            user = User(student1=student1,reg_no=reg_no,email=email,tel=tel,
                        password_hash=password,course=course)
            
            db.session.add(user)
            db.session.commit()
            return data
                #flash('status registration completed.')
        else:
            return {'error':'Could not creat account'}


class Login1(Resource):
    def post(self):
        auth = request.authorization
        data = request.get_json()
        
        '''checking if authorization information is complete'''
        if not data or not data['username'] or not data['password']:
            return make_response('Could not verify1',401,{'www-Authenticate':'Basic realm-"login required!"'})        
        admin = User.query.filter_by(reg_no=data['username']).first()
        if not admin:
            return make_response('Could not verify2',401,{'www-Authenticate':'Basic realm-"login required!"'})       
        if check_password_hash(admin.password_hash,data['password']):
            token = jwt.encode({'reg_no':admin.reg_no,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60)},app.config['SECRET_KEY'])
            return jsonify({'token':token.decode('UTF-8'),'username':admin.reg_no})
        return make_response('Could not verify3',401,{'www-Authenticate':'Basic realm-"login required!"'})


class Logout1(Resource):
#    @token_required
##    @staticmethod
##    @login_required
    def post(current_user):
        logout_user()
        flash('You were logged out.')
##        return redirect(url_for(''))


class ResetPassword(Resource):
    
    def post(self):
        data=request.get_json()
        old_pass, new_pass = generate_password_hash(data['old_pass']), generate_password_hash(data['new_pass'])
        user = User.query.filter_by(reg_no=data['reg_no']).first()
        user.password_hash =  new_pass
        db.session.commit()
        return {"status":"success"}
        
        
                
class GetAllProjects(Resource):
    #@token_required
    def get(self,current_user):
        project = Project.query.all()
        return [x.json() for x in project]


class PostProposals(Resource):
    #@token_required
##    @staticmethod  
    def post(current_user):

        data = request.form
        
        reg_nox = data['reg_nox']
        title = data['title']
        #reg_no = data['reg_no']
        proposal_ref = data['proposal_ref']
        problem_statement = data['problem_statement']
        methodology = data['methodology']
        try:
            user = User.query.filter_by(reg_no=reg_nox).first()
            reg_no = user.reg_no
            student1 = user.student1
            try:
                
                if Partner_table.query.filter_by(reg_no=reg_no).first() != None:
                    partner = Partner_table.query.filter_by(reg_no=reg_no).first()
                    status = partner.status1
                    if status == 'Accepted':
                        if partner.reg_no == data['reg_nox']:
                            reg_no2 = partner.reg_no2
                        else:
                            reg_no2 = partner.reg_no

                        partner2 = User.query.filter_by(reg_no=reg_no2).first()
                        student2 = partner2.student1

                    else:
                        pass

                else:
                    
                    partner = Partner_table.query.filter_by(reg_no2=reg_no).first()
                    status = partner.status1
                    
                    if status == 'Accepted':
                        if partner.reg_no2 == data['reg_nox']:
                            reg_no2 = partner.reg_no
                            
                        else:
                            reg_no2 = partner.reg_no2
                        partner2 = User.query.filter_by(reg_no=reg_no2).first()
                        
                        student2 = partner2.student1
                        

                    else:
                        pass
                    

            except Exception:
                reg_no2 = ""
                student2 = ""
            
            file = request.files['file']
            
            filename = secure_filename(file.filename)
            fileExt = filename.split('.')[1]
            autoGenFileName = student1+'_'+student2+str(datetime.datetime.today().strftime("%d-%m-%Y"))
            newFilename = str(autoGenFileName)+'.'+fileExt
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],newFilename))

            

            status = 'pending'
            supervisor = 'None'
            email = 'None'
            comment = 'None'
            cosupervisor = ''
            extsupervisor =''
            review_supervisor = ''
            review_comment = ''
            
            id = ''
            

            p_upload = Proposal(id=id,title=title,reg_no=reg_no,project_ref=proposal_ref,problem_statement=problem_statement,
                                methodology=methodology ,reg_no2=reg_no2,proposal_uploadfile=newFilename,
                                status=status,supervisor=supervisor,email=email,
                                comment=comment,student1=student1,student2=student2,cosupervisor=cosupervisor,extsupervisor=extsupervisor,
                                review_supervisor=review_supervisor,review_comment=review_comment)

            
            db.session.add(p_upload)
            db.session.commit()
            

            try:
                mess=Admin.query.all()
            
                for mes in mess:
                    message = 'Proposal Submitted by '+student1+' and '+student2+' on ' + str(datetime.datetime.today())
                    subject = 'Proposal Submitted: NO REPLY'
                    sender = 'fypmailing@gmail.com'
                    msg = Message(sender=sender,recipients=[mes.email],body=message,subject=subject)
                    
                    with app.open_resource(str(os.path.join(app.config['UPLOAD_FOLDER'],newFilename))) as fp:
                        msg.attach(newFilename,"file/pdf",fp.read())
                        mail.send(msg)

            except Exception:
                return {'error':'mail not sent'}
        except Exception:
            return {'status':'Posting proposal failed'}
                
        

    def delete(current_user):
        data = request.get_json()
        prop=Proposal.query.filter_by(title=data['title']).first()
        db.session.delete(prop)
        db.session.commit()
        return {'status':'succces'}

    def put(self,current_user):
        data = request.get_json()
        prop=Proposal.query.filter_by(title=data['title']).first()
        prop.title=request.json.get('title',prop.title)
        prop.problem_statment=request.json.get('problem_statment',prop.problem_statment)
        prop.abstract=request.json.get('abstract',prop.abstract)
        prop.proposal_uploadfile=request.json.get('proposal_uploadfile',prop.proposal_uploadfile)
        prop.student_pair=request.json.get('student_pair',prop.student_pair)
        db.session.commit()
        return jsonify({'pro':prop})
         
class ViewPrjects(Resource):
    #@token_required
##    @staticmethod
    def post(current_user):
        data = request.get_json()
        #error = None
        
        try:
            project = Proposal.query.filter_by(reg_no=str(data['reg_no']))
            
            if [x.json() for x in project] != []:
                return [x.json() for x in project]

            else:
                project2 = Proposal.query.filter_by(reg_no2=str(data['reg_no']))
                return [x.json() for x in project2]

        except Exception:
            return {'Error':'No recodes available'}
                        
class ViewProposals(Resource):
    #@token_required
##    @staticmethod
    def get(current_user):
        students = Project.query.all()
        return [x.json() for x in students]
        
class PostProgressReport(Resource):
    #@token_required
    def post(current_user):

        data = request.form
        date_s = datetime.datetime.today()
        
        datestamp = date_s.strftime('%d-%m-%Y')
        reg_no1 = data['reg_no']
        comment = data['comment']

        file = request.files['file']
        filename = secure_filename(file.filename)
        
        fileExt = filename.split('.')[1]
        autoGenFileName = student1+'_'+student2+str(datetime.datetime.today().strftime("%d-%m-%Y"))

        newFilename = str(autoGenFileName)+'.'+fileExt

        file.save(os.path.join(app.config['UPLOAD_FOLDER'],newFilename))
        
        try:
            if Proposal.query.filter_by(reg_no=reg_no1).first() is not None:
                supervisor = Proposal.query.filter_by(reg_no=reg_no1).first()
                s_email = supervisor.email

                progress = Progress_report(reg_no=reg_no1,files=newFilename,supervisor_email=s_email,datestamp=datestamp,comment=comment)
                db.session.add(progress)
                db.session.commit()

                return data
            else:
                supervisor2 = Proposal.query.filter_by(reg_no2=reg_no1).first()
                s_email = supervisor2.email

                progress = Progress_report(reg_no=reg_no1,files=newFilename,supervisor_email=s_email,datestamp=datestamp,comment=comment)
                db.session.add(progress)
                db.session.commit()

                return data

            try:
        
        
                message = 'Progress Report Submitted by '+student1+' and '+student2+' on ' + str(datetime.datetime.today())
                subject = 'Progress Report Submitted: NO REPLY'
                sender = 'fypmailing@gmail.com'
                msg = Message(sender=sender,recipients=[s_email],body=message,subject=subject)
                mail.send(msg)

            except Exception:
                return {'error':'mail not sent'}

        except Exception:
            return {'error':'submission failed'}
                

class Previous_topics_by_title(Resource):
    #@token_required
    def get(current_user):
        data = request.get_json()
        topic = Previous_topic.query.filter_by(title=data['title']).first()
        try:
            return topic.json()
        except Exception:
            return {'title':'No data available'}

class Previous_topics_by_year(Resource):
#    @token_required
    def get(current_user):
        data = request.get_json()
        topic = Previous_topic.query.all()
#        try:
        return [x.json() for x in topic]
        
#        except Exception:
#            return "No reports available for that year"

class UpdateMethodology(Resource):
#    @token_required
    def post(current_user):
        data = request.get_json()
        update = Proposal.query.filter_by(reg_no=data['reg_no']).first()
        update.methodology = data['methodology']
        db.session.commit()

class resubmitfiles(Resource):
#    @token_required
    def post(current_user):
        data = request.get_json()
        update = Proposal.query.filter_by(reg_no=data['reg_no']).first()

        file = request.files['file']
        filename = secure_filename(file.filename)
        
        fileExt = filename.split('.')[1]
        autoGenFileName = student1+'_'+student2+str(datetime.datetime.today().strftime("%d-%m-%Y"))

        newFilename = str(autoGenFileName)+'.'+fileExt

        file.save(os.path.join(app.config['UPLOAD_FOLDER'],newFilename))

        update.proposal_uploadfile = newFilename
        db.session.commit()

class deleteproposal(Resource):
#    @token_required
    def post(current_user):
        data = request.get_json()
        update = Proposal.query.filter_by(reg_no=data['reg_no']).first()
        db.session.delete(update)
        db.session.commit()
        return data

class deleteprogressreport(Resource):
#    @token_required
    def post(current_user):
        data = request.get_json()
        update = Progress_report.query.filter_by(datestamp=data['datestamp']).first()
        db.session.delete(update)
        db.session.commit()

class addpartner(Resource):
#    @token_required
    def post(current_user):
        data = request.get_json()
        
        if Partner_table.query.filter_by(reg_no=data['reg_no']).first() is not None:
            return {'Error':'Student pair already exist'}

        else:
            
            if Partner_table.query.filter_by(reg_no2=data['reg_no']).first() is not None:
                return {'Error':'Student pair already exist'}

            else:
                
                if Partner_table.query.filter_by(reg_no=data['reg_no2']).first() is not None:
                    return {'Error':'Student pair already exist'}

                else:
                    if Partner_table.query.filter_by(reg_no2=data['reg_no2']).first() is not None:
                        return {'Error':'Student pair already exist'}

                    else:
                        reg_no = data['reg_no']
                        reg_no2 = data['reg_no2']
                        status ="pending"
                        partner = Partner_table(reg_no=reg_no,reg_no2=reg_no2,status1=status)
                        db.session.add(partner)
                        db.session.commit()
                        return data

class viewpartnerequest(Resource):
#    @token_required
    def post(current_user):
        data = request.get_json()
        try:
            if Partner_table.query.filter_by(reg_no2=data['reg_no']).first() is not None:
                partner  = Partner_table.query.filter_by(reg_no2=data['reg_no']).first()
                return partner.json()
            else:
                partner  = Partner_table.query.filter_by(reg_no=data['reg_no']).first()
                return partner.json()

        except Exception:
            return {'error':'No student exist'}

class confirmreguest(Resource):
#    @token_required
    def post(current_user):
        data = request.get_json()
        
        response = data['response']
        try:
            partner  = Partner_table.query.filter_by(reg_no2=data['reg_no']).first()
        
            reg_no1 = partner.reg_no
            partner2 = User.query.filter_by(reg_no=reg_no1).first()

            if response == 'accept':
                partner.status1 = 'Accepted'
                db.session.commit()
                
                try:
                    
                    message = 'Final year project partner request accepted'
                    subject = 'Request Accepted: NO REPLY'
                    sender = 'fypmailing@gmail.com'
                    
                    msg = Message(sender=sender,recipients=[partner2.email],body=message,subject=subject)
                    
                    mail.send(msg)
                   
                    
                    

                except Exception:
                    return {'error':'mail not sent'}

            elif response == 'reject':
                db.session.delete(partner)
                db.session.commit()
                
                try:
                    
                    message = 'Your request for a project partner has been rejected'
                    subject = 'Request Rejected: NO REPLY'
                    sender = 'fypmailing@gmail.com'
                    msg = Message(sender=sender,recipients=[partner2.email],body=message,subject=subject)
                    mail.send(msg)

                except Exception:
                    return {'error':'mail not sent'}
            else:
                return{"eror":"request failed"}
            
        except Exception:
            return {'error':'Only the second student can confirm'}
            
        

class viewpartner(Resource):
    #@token_required
    def get(current_user):
        data = request.get_json()
        try:
            if Partner_table.query.filter_by(reg_no=data['reg_no']).first() is not None:
                topic = Partner_table.query.filter_by(reg_no=data['reg_no']).first()
                return topic.json()

            else:
                topic = Partner_table.query.filter_by(reg_no2=data['reg_no']).first()
                return topic.json()
        
        except Exception:
            return {'title':'No data available'}







