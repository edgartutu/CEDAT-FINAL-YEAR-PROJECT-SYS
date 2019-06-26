from project import app, db
from flask_restful import Resource, Api
from flask_restful import Api
from project.users.views import Register,Login1,Logout,ResetPassword,GetAllProjects,PostProposals,ViewPrjects,ViewProposals
from project.guest.views import Login2,Logout,AssignedProposal,PostProject_
from project.admin.views import Login,Logout,ApproveProject,PostProject,PendingProposal,ProposalComment



api = Api(app)



api.add_resource(Register, '/register/<string:email>/<string:reg_no>/<string:password>')
api.add_resource(Login1, '/login-user')
api.add_resource(Logout, '/logout')
##api.add_resource(ResetPassword, '/reset-password')
api.add_resource(GetAllProjects, '/getprojects')
api.add_resource(PostProposals, '/postproposals/<string:title>/<string:reg_no>/<string:problem_statement>/<string:abstract>/<string:student_pair>/<string:proposal_uploadfile>',endpoint='postproposals')
api.add_resource(PostProposals, '/postproposals/del/<string:title>',endpoint='postproposals-del')
api.add_resource(ViewPrjects, '/viewprojects')
api.add_resource(ViewProposals, '/viewproposals')
##
api.add_resource(Login, '/login-admin')
##api.add_resource(Logout, '/logout-user')
api.add_resource(ApproveProject, '/approve')
##api.add_resource(PostProject, '/postproject')
##api.add_resource(PostProject, '/postproject/<string:title>/<string:comments>')
api.add_resource(PostProject, '/postproject/del/<string:title>', endpoint='postproject-del')
api.add_resource(PendingProposal, '/pendingproposal')
api.add_resource(ProposalComment, '/proposalcomment/<string:comment>')
##
##api.add_resource(Login2, '/login-guest')
##api.add_resource(Logout, '/logout-guest')
api.add_resource(AssignedProposal, '/viewproposals')
api.add_resource(PostProject_, '/pro/<string:title>/<string:comments>')
api.add_resource(PostProject_, '/pro/delete/<string:title>',endpoint='project-delete')

         

if __name__ == '__main__':
    app.run(debug=True)
