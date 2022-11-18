
from flask_restful import Resource, Api
from flask_restful import fields, marshal_with,reqparse
from flask_restful import reqparse
from application.validation import BusinessValidationError, NotFoundError
from application.models import List,User,Card
from application.database import db
from flask import current_app as app
import werkzeug
from application import tasks
from flask import abort
from flask_security import auth_required, login_required, roles_accepted, roles_required, auth_token_required

User_output_fields={
    'id':fields.Integer,
    "Name":fields.String,
    "email":fields.String,
    "password":fields.String,
    "fs_uniquifier":fields.String,
    "active":fields.String
}

List_output_fields={
    'User_Id':fields.Integer,
    'List_Id':fields.Integer,
    "Name":fields.String,
    "Description":fields.String
}

Card_output_fields={
    'List_Id':fields.Integer,
    'Card_Id':fields.Integer,
    'Deadline':fields.String,
    "Content":fields.String,
    "Status":fields.String,
    "Title":fields.String
}

create_user_parser=reqparse.RequestParser()
create_user_parser.add_argument('id')
create_user_parser.add_argument('password')
create_user_parser.add_argument('email')
create_user_parser.add_argument('fs_uniquifier')
create_user_parser.add_argument('Name')
create_user_parser.add_argument('active')

update_user_parser=reqparse.RequestParser()
update_user_parser.add_argument('id')
update_user_parser.add_argument('password')
update_user_parser.add_argument('email')
# update_user_parser.add_argument('SecretKey')
update_user_parser.add_argument('Name')

create_list_parser=reqparse.RequestParser()
create_list_parser.add_argument('List_Id')
create_list_parser.add_argument('User_Id')
create_list_parser.add_argument('Description')
create_list_parser.add_argument('Name')

update_list_parser=reqparse.RequestParser()
update_list_parser.add_argument('List_Id')
update_list_parser.add_argument('User_Id')
update_list_parser.add_argument('Name')
update_list_parser.add_argument('Description')

create_card_parser=reqparse.RequestParser()
create_card_parser.add_argument('List_Id')
create_card_parser.add_argument('Card_Id')
create_card_parser.add_argument('Title')
create_card_parser.add_argument('Content')
create_card_parser.add_argument('Deadline')
create_card_parser.add_argument('Status')

update_card_parser=reqparse.RequestParser()
update_card_parser.add_argument('List_Id')
update_card_parser.add_argument('Card_Id')
update_card_parser.add_argument('Title')
update_card_parser.add_argument('Content')
update_card_parser.add_argument('Deadline')
update_card_parser.add_argument('Status')


test_api_resource_fields = {
    'msg':    fields.String,
}




class UserAPI(Resource):
    @marshal_with(User_output_fields)
    @auth_required("token")
    def get(self,User_Id,password):
        id=int(User_Id)
        user=db.session.query(User).filter(User.id==id,User.password==password).first()
        print(user)
    
        if user:
            return user
        else:
            raise NotFoundError(status_code=404)

    def put(self,User_Id,password):
        id=int(User_Id)
        args=update_user_parser.parse_args()
        passw=args.get('password',None)
        em=args.get("email",None)
        # key=args.get('SecretKey',None)
        nam=args.get('Name',None)
        user=db.session.query(User).filter(User.User_Id==id,User.password==password).first()
        print(user)
        if user:
            user.Name=nam
            user.email=em
            user.password=passw
            db.session.commit()
            return user
        else:
            raise NotFoundError(status_code=404)

    def delete(self,User_Id,password):
        id=int(User_Id)
        user=db.session.query(User).filter(User.User_Id==id,User.password==password).first()
        print(user)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {},201
        else:
            raise NotFoundError(status_code=404)

    @auth_required("token")
    def post(self):
        args=create_user_parser.parse_args()
        print(args)
        user_id=args.get("User_Id",None)
        password=args.get("password",None)
        em=args.get("email",None)
        nam=args.get('Name',None)
        print("User id")
        print(user_id)
        print("password")
        print(password)
        if user_id is None or password is None:
            raise BusinessValidationError(status_code=400,error_code="BE1001",error_message="user_id or password is required")
        else:
            pass
        user=db.session.query(User).filter(User.User_Id==int(user_id)).first()
        if user:
            raise BusinessValidationError(status_code=400,error_code="BE1002",error_message="duplicate user_id")
        new_user=User(User_Id=int(user_id),password=password,Name=nam,email=em)
        db.session.add(new_user)
        db.session.commit()
        return {},201



class ListAPI(Resource):
    @marshal_with(List_output_fields)
    @auth_required("token")
    def get(self,User_Id):
        id=int(User_Id)
        user=db.session.query(User).filter(User.id==id).first()
        NewL={}
        if user:
            list=db.session.query(List).filter(List.User_Id==id).all()
            print(type(list))
            AllCards={}
            print(type(NewL))
            for l in list:
                NewL[l.List_Id]={}
                NewL[l.List_Id]["List"]=l
                NewL[l.List_Id]["Cards"]=db.session.query(Card).filter(Card.List_Id==l.List_Id).all()
            # list.append(NewL)
            print("Modified list")
            print(NewL)
            if list:
                print("Found List")
                return list
            else:
                raise NotFoundError(status_code=404)
        else:
            raise NotFoundError(status_code=404)

    @auth_required("token")
    def put(self,User_Id,List_Id):
        id=int(User_Id)
        id2=int(List_Id)
        args=update_list_parser.parse_args()
        name=args.get('Name',None)
        description = args.get("Description")
        list=db.session.query(List).filter(List.User_Id==id,List.List_Id==id2).first()
        list.Name=name
        list.Description=description
        db.session.commit()
        return {},201
        
    @auth_required("token")
    def delete(self,User_Id,List_Id):
        id=int(User_Id)
        id2=int(List_Id)
        list1=db.session.query(List).filter(List.User_Id==id,List.List_Id==id2).first()
        db.session.delete(list1)
        db.session.commit()
        return {},201

    @auth_required("token")
    def post(self,User_Id):
        id=int(User_Id)
        args=create_list_parser.parse_args() 
        Nam=args.get('Name',None)
        Descriptio=args.get('Description',None)
        print("DESC")
        print(Descriptio)
        new_list=List(Name=Nam,User_Id=id,Description=Descriptio)
        db.session.add(new_list)
        db.session.commit()
        return {},201
        # if id is None or password is None:
        #     raise BusinessValidationError(status_code=400,error_code="BE1001",error_message="user_id or password is required")
        # else:
        #     pass
        # user=db.session.query(User).filter(User.User_Id==int(id)).first()
        # if user:
        #     raise BusinessValidationError(status_code=400,error_code="BE1002",error_message="duplicate user_id")


class OneListAPI(Resource):
    @marshal_with(List_output_fields)
    @auth_required("token")
    def get(self,User_Id,Name):
        id=int(User_Id)
        name=Name.replace("%20", " ")
        name=name[1:-1]
        print(name)
        list=db.session.query(List).filter(List.User_Id==id,List.Name==name).first()
        print(list)
        return list

class CardAPI(Resource):
    @marshal_with(Card_output_fields)
    @auth_required("token")
    def get(self,List_Id):
            id2=int(List_Id)
            card=db.session.query(Card).filter(Card.List_Id==id2).all()
            if card:
                print(card)
                return card
            else:
                print("Nothing")
                # raise NotFoundError(status_code=404)
            # else:
            #     raise NotFoundError(status_code=404)        
        # else:
        #     raise NotFoundError(status_code=404)
    @auth_required("token") 
    def put(self,User_Id,Card_Id):
        id=int(User_Id)
        id2=int(Card_Id)
        args=update_card_parser.parse_args()
        Content=args.get('Content',None)
        Deadline=args.get("Deadline",None)
        Status=args.get('Status',None)
        Title = args.get('Title',None)
        List_id = args.get('List_Id',None)
        print(List_id)
        card=db.session.query(Card).filter(Card.Card_Id==id2).first()
        if card:
            # if Content is not None:
            card.Content = Content
            # if Deadline is not None:
            card.Deadline = Deadline
            # if Status is not None:
                # card.Status=Status
            card.Status = Status
            # if Title is not None:
            card.Title = Title
            # if List_id is not None:
            card.List_Id = List_id
        db.session.commit()
        return {},201
        # else:
        #     raise NotFoundError(status_code=404)
    @auth_required("token") 
    def delete(self,User_Id,Card_Id):
        id3=int(Card_Id)
        id=int(User_Id)
        card=db.session.query(Card).filter(Card.Card_Id==id3).first()
        db.session.delete(card)
        db.session.commit()
        return {},201
        #         else:
        #             raise NotFoundError(status_code=404)
        #     else:
        #         raise NotFoundError(status_code=404)        
        # else:
        #     raise NotFoundError(status_code=404)

    @auth_required("token")     
    def post(self,User_Id,List_Id):
        e=int(User_Id)
        id1=int(List_Id)
        args=create_card_parser.parse_args()
        content=args.get('Content',None)
        deadline=args.get("Deadline",None)
        status=args.get('Status',None)
        Titl = args.get('Title',None)
        new_card=Card(Title=Titl,Content=content,Deadline=deadline,Status=status,List_Id =id1)
        db.session.add(new_card)
        db.session.commit()
        return {},201
        #     else:
        #         raise BusinessValidationError(status_code=400,error_code="BE1003",error_message="List_Id is invalid")
        # if id is None or password is None:
        #     raise BusinessValidationError(status_code=400,error_code="BE1001",error_message="user_id or password is required")
        # else:
        #     pass
        # user=db.session.query(User).filter(User.User_Id==int(id)).first()
        # if user:
        #     raise BusinessValidationError(status_code=400,error_code="BE1002",error_message="duplicate user_id")




class OneCardAPI(Resource):
    @marshal_with(Card_output_fields)
    @auth_required("token")
    def get(self,User_Id,Title):
        print("INSIDE ONECARD API")
        id=int(User_Id)
        title=Title.replace("%20", " ")
        title=title[1:-1]
        print(title)
        card=db.session.query(Card).filter(Card.Title==title).first()
        print(card)
        return card



class SendImage_Logs(Resource):        
    def get(self,User_Id,password,List_Id):
        id=int(User_Id)
        id1=int(List_Id)
        user=db.session.query(User).filter(User.User_Id==id,User.password==password).first()
        if user:
            tracker=db.session.query(List).filter(List.User_Id==id,List.List_Id==id1).first()
            print('jh')
            if tracker:
                q='192.168.1.19:8080/Dashboard/'+str(id)+'/'+str(id1)+'/Visualize'
                return {'link':q}
        else:
            return "Image sending failed"

# @app.route("/")
# @app.route("/Dashboard/<String:User_Id>/Export_User", methods=["GET", "POST"])
# def hello():

#     job = tasks.export_user.apply_async(countdown =10,expires =120)
#     # job = tasks.print_current_time_job.apply_async(eta=now+timedelta(seconds=10))
#     result = job.wait()
#     return str(result), 200
