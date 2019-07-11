from project import app, db
from flask_restful import Resource, Api
from flask_restful import Api
from project.users.views import Register,Login1,Logout1,ResetPassword,GetAllProjects,PostProposals,ViewPrjects,ViewProposals,PostProgressReport,Previous_topics_by_title,Previous_topics_by_year,UpdateAbstract
from project.guest.views import Login2,Logout2,AssignedProposal,PostProject_,Reports,ProgressComment
from project.admin.views import Login,Logout,ApproveProject,PostProject,PendingProposal,ProposalComment,ApprovedProposal,viewprojects,viewrejected,allstudents,allguest



api = Api(app)

api.add_resource(Register, '/register/<string:email>/<string:reg_no>/<string:password>')
api.add_resource(Login1, '/login-user')
api.add_resource(Logout1, '/logout')
##api.add_resource(ResetPassword, '/reset-password')
api.add_resource(GetAllProjects, '/getprojects')
api.add_resource(PostProposals, '/postproposals')
api.add_resource(PostProposals, '/postproposals/del',endpoint='postproposals-del')
api.add_resource(ViewPrjects, '/viewprojects2')
api.add_resource(ViewProposals, '/viewpostedprojects')
api.add_resource(PostProgressReport, '/postprogressreport')
api.add_resource(Previous_topics_by_title, '/filterprevioustopicbytitle')
api.add_resource(Previous_topics_by_year, '/filterprevioustopicbyyear')
api.add_resource(UpdateAbstract, '/updateabstract')
##
api.add_resource(Login, '/login-admin')
api.add_resource(Logout, '/logout-user')
api.add_resource(ApproveProject, '/approve')
api.add_resource(PostProject, '/postproject')
api.add_resource(PostProject, '/postproject/del/<string:title>', endpoint='postproject-del')
api.add_resource(PendingProposal, '/pendingproposal')
api.add_resource(ProposalComment, '/proposalcomment')
api.add_resource(ApprovedProposal, '/approved')
api.add_resource(viewprojects, '/adminviewprojects')
api.add_resource(viewrejected, '/viewrejected')
# Not yet connected to admin dash board
api.add_resource(allstudents, '/allstudents')
api.add_resource(allguest, '/allguest')
#api.add_resource(allprogressreports, '/allprogressreports')
##
api.add_resource(Login2, '/login-guest')
api.add_resource(Logout2, '/logout-guest')
api.add_resource(AssignedProposal, '/viewproposals')
api.add_resource(PostProject_, '/pro/<string:title>/<string:comments>')
api.add_resource(PostProject_, '/pro/delete/<string:title>',endpoint='project-delete')
api.add_resource(ProgressComment, '/progresscomment')
api.add_resource(Reports, '/reports')

if __name__ == '__main__':
    app.run(debug=True)

