from flask_restful import Resource,fields,marshal_with,reqparse
from application.database import db
from application.models import User,Assesment,Thread,Post,Connection,Message,Aspirant
from application.validation import NotFoundError,BusinessValidationError
from datetime import datetime
import pytz
from sqlalchemy import func

user_output_fields={
    'user_id':fields.Integer,
    "Name":fields.String,
    "email":fields.String,
    "password":fields.String,
    "Category":fields.String
}



assesment_output_fields={
    'creator_id':fields.Integer,
    'assesment_id':fields.Integer,
    'Student_Count':fields.Integer,
    'Quiz':fields.String,
    'Toppers':fields.String,
    'Name':fields.String
}

aspirant_output_fields={
    'aspirant_id':fields.Integer,
    'assesment_id':fields.Integer,
    'aspirant_score':fields.Integer,
    'aspirant_name':fields.String
}

thread_output_fields={
    'user_id':fields.Integer,
    'thread_id':fields.Integer,
    'Thread_count':fields.Integer,
    'Thread_Map':fields.String,
    'Title':fields.String
}

post_output_fields={
    'thread_id':fields.Integer,
    'post_id':fields.Integer,
    'Post_Message':fields.String,
    'Annoynmous':fields.String,
    'Post_Date_Time':fields.String,
    'Poster_Name': fields.String,
    'Poster_email': fields.String
}

connection_output_fields={
    'sender_id':fields.Integer,
    'receiver_id':fields.Integer,
    'connection_id':fields.Integer,
    'Approval_Status':fields.String,
    'Connection_Map':fields.String,
    'Sender_Name': fields.String,
    'Receiver_Name': fields.String,
    "Request": fields.String
}

message_output_fields={
    'connection_id':fields.Integer,
    'message_id':fields.Integer,
    'Content':fields.String,
    "Message_Date_Time":fields.String,
    "Message_Sender":fields.String
}


create_user_parser=reqparse.RequestParser()
create_user_parser.add_argument('user_id')
create_user_parser.add_argument('password')
create_user_parser.add_argument('email')
create_user_parser.add_argument('Name')
create_user_parser.add_argument('Category')

update_user_parser=reqparse.RequestParser()
update_user_parser.add_argument('id')
update_user_parser.add_argument('password')
update_user_parser.add_argument('email')
update_user_parser.add_argument('Name')
update_user_parser.add_argument('Category')


create_assesment_parser=reqparse.RequestParser()
create_assesment_parser.add_argument('creator_id')
create_assesment_parser.add_argument('assesment_id')
create_assesment_parser.add_argument('Student_count')
create_assesment_parser.add_argument('Quiz')
create_assesment_parser.add_argument('Toppers')
create_assesment_parser.add_argument('Name')


update_assesment_parser=reqparse.RequestParser()
update_assesment_parser.add_argument('creator_id')
update_assesment_parser.add_argument('assesment_id')
update_assesment_parser.add_argument('Student_Count')
update_assesment_parser.add_argument('Quiz')
update_assesment_parser.add_argument('Toppers')
update_assesment_parser.add_argument('Name')


create_aspirant_parser=reqparse.RequestParser()
create_aspirant_parser.add_argument('assesment_id')
create_aspirant_parser.add_argument('aspirant_id')
create_aspirant_parser.add_argument('aspirant_score')
create_aspirant_parser.add_argument('aspirant_name')

update_aspirant_parser=reqparse.RequestParser()
update_aspirant_parser.add_argument('assesment_id')
update_aspirant_parser.add_argument('aspirant_id')
update_aspirant_parser.add_argument('aspirant_score')
update_aspirant_parser.add_argument('aspirant_name')

create_thread_parser=reqparse.RequestParser()
create_thread_parser.add_argument('user_id')
create_thread_parser.add_argument('thread_id')
create_thread_parser.add_argument('Thread_count')
create_thread_parser.add_argument('Title')
create_thread_parser.add_argument('Thread_Map')


update_thread_parser=reqparse.RequestParser()
update_thread_parser.add_argument('user_id')
update_thread_parser.add_argument('thread_id')
update_thread_parser.add_argument('Thread_count')
update_thread_parser.add_argument('Title')
update_thread_parser.add_argument('Thread_Map')


create_post_parser=reqparse.RequestParser()
create_post_parser.add_argument('post_id')
create_post_parser.add_argument('thread_id')
create_post_parser.add_argument('Post_Message')
create_post_parser.add_argument('Annoynmous')
create_post_parser.add_argument("Post_Date_Time")
create_post_parser.add_argument("Poster_email")
create_post_parser.add_argument("Poster_Name")


update_post_parser=reqparse.RequestParser()
update_post_parser.add_argument('post_id')
update_post_parser.add_argument('thread_id')
update_post_parser.add_argument('Post_Message')
update_post_parser.add_argument('Annoynmous')
update_post_parser.add_argument("Post_Date_Time")
update_post_parser.add_argument("Poster_email")
update_post_parser.add_argument("Poster_Name")

create_connection_parser=reqparse.RequestParser()
create_connection_parser.add_argument('sender_id')
create_connection_parser.add_argument('receiver_id')
create_connection_parser.add_argument('Sender_Name')
create_connection_parser.add_argument('Receiver_Name')
create_connection_parser.add_argument('connection_id')
create_connection_parser.add_argument('Connection_Map')
create_connection_parser.add_argument('Approval_Status')
create_connection_parser.add_argument('Request')


update_connection_parser=reqparse.RequestParser()
update_connection_parser.add_argument('sender_id')
update_connection_parser.add_argument('receiver_id')
update_connection_parser.add_argument('connection_id')
update_connection_parser.add_argument('Connection_Map')
update_connection_parser.add_argument('Approval_Status')
update_connection_parser.add_argument('Sender_Name')
update_connection_parser.add_argument('Receiver_Name')
update_connection_parser.add_argument('Request')


create_message_parser=reqparse.RequestParser()
create_message_parser.add_argument('connection_id')
create_message_parser.add_argument('message_id')
create_message_parser.add_argument('Content')
create_message_parser.add_argument('Message_Date_Time')
create_message_parser.add_argument('Message_Sender')

update_message_parser=reqparse.RequestParser()
update_message_parser.add_argument('connection_id')
update_message_parser.add_argument('message_id')
update_message_parser.add_argument('Content')
update_message_parser.add_argument('Message_Date_Time')
update_message_parser.add_argument('Message_Sender')


class TopAssesmentsAPI(Resource):
    @marshal_with(assesment_output_fields)
    def get(self,user_id,password):
        id=int(user_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            assesment=db.session.query(Assesment).filter().order_by(Assesment.Student_Count.desc()).limit(3).all()
            if assesment:
                return assesment
            else:
                raise NotFoundError(status_code=404)
        else:
            raise NotFoundError(status_code=404)
            
            
class TopPostAPI(Resource):
    @marshal_with(post_output_fields)
    def get(self,user_id,password):
        print("INSIDE Posts")
        id=int(user_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            posts=db.session.query(Post).all()
            post1 =db.session.query(Post.Poster_Name,func.count(Post.Poster_Name)).group_by(Post.Poster_Name).all()
            sorted_data = sorted(post1, key=lambda x: x[1], reverse=True)
            top3_counts = sorted_data[:3]
            FinalPost=[]
            for i in top3_counts:
                temp=db.session.query(Post).filter(Post.Poster_Name==i[0]).first()
                FinalPost.append(temp)
            print(FinalPost)
            return FinalPost
        else:
            raise NotFoundError(status_code=404)
                
                
class TopThreadsAPI(Resource):
    @marshal_with(thread_output_fields)
    def get(self,user_id,password):
        print("INSIDE THREADS")
        id=int(user_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            thread=Thread.query.order_by(Thread.Thread_count.desc()).limit(3).all()
            print(thread)
            if thread:
                return thread
            else:
                raise NotFoundError(status_code=404)





class UserAPI(Resource):
    @marshal_with(user_output_fields)
    def get(self,email_id,password):
        print('Hello')
        print(email_id)
        print(password)
        user=db.session.query(User).filter(User.email==email_id,User.password==password).first()
        print(user)
        if user:
            return user
        else:
            raise NotFoundError(status_code=404)

    @marshal_with(user_output_fields)
    def put(self,user_id,password):
        id=int(user_id)
        args=update_user_parser.parse_args()
        passw=args.get('password',None)
        em=args.get("email",None)
        nam=args.get('Name',None)
        cat=args.get("Category",None)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        print(user)
        if user:
            user.Name=nam
            user.email=em
            user.password=passw
            user.Category=cat
            db.session.commit()
            return user
        else:
            raise NotFoundError(status_code=404)

    def delete(self,user_id,password):
        id=int(user_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        print(user)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {},201
        else:
            raise NotFoundError(status_code=404)
        
    def post(self):
        print("INSIDE")
        args=create_user_parser.parse_args()
        print("IN API.")
        password=args.get('password',None)
        em=args.get("email",None)
        nam=args.get('Name',None)
        cat=args.get("Category",None)
        print("Password"+password)
        print("email "+em)
        print("name"+nam)
        new_user=User(password=password,Name=nam,email=em,Category=cat)
        print(new_user)
        db.session.add(new_user)
        db.session.commit()
        return {},201


class AllThreadsAPI(Resource):
    @marshal_with(thread_output_fields)
    def get(self,user_id,password):
        print("INSIDE THREADS")
        id=int(user_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            thread=Thread.query.order_by(Thread.Thread_Map.desc()).all()
            print(thread)
            if thread:
                return thread
            else:
                raise NotFoundError(status_code=404)

class AllThreadsUserAPI(Resource):
    @marshal_with(thread_output_fields)
    def get(self,user_id,password):
        print("INSIDE THREADS")
        id=int(user_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            thread=Thread.query.filter(Thread.user_id==id).order_by(Thread.Thread_Map.desc()).all()
            print(thread)
            if thread:
                return thread
            else:
                raise NotFoundError(status_code=404)

class AllPostAPI(Resource):
    @marshal_with(post_output_fields)
    def get(self,user_id,password,thread_id):
        print("INSIDE THREADS")
        id=int(user_id)
        id2=int(thread_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()

        if user:
            thread=db.session.query(Thread).filter(Thread.thread_id==id2).first()
            print(thread)
            if thread:
                posts=db.session.query(Post).filter(Post.thread_id==id2).order_by(Post.Post_Date_Time.asc()).all()
                return posts
            else:
                raise NotFoundError(status_code=404)
            
class AllMessageAPI(Resource):
    @marshal_with(message_output_fields)
    def get(self,user_id,password,connection_id):
        print("INSIDE CONNECTIONS")
        id=int(user_id)
        id2=int(connection_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()

        if user:
            con=db.session.query(Connection).filter(Connection.connection_id==id2).first()
            print(con)
            if con:
                sms=db.session.query(Message).filter(Message.connection_id==id2).order_by(Message.Message_Date_Time.asc()).all()
                return sms
            else:
                raise NotFoundError(status_code=404)
            
class AllAssesmentsUserAPI(Resource):
    @marshal_with(assesment_output_fields)
    def get(self,user_id,password):
        id=int(user_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            assesment=db.session.query(Assesment).filter(Assesment.creator_id==id).all()
            if assesment:
                return assesment
            else:
                raise NotFoundError(status_code=404)
        else:
            raise NotFoundError(status_code=404)

class AllAssesmentsAPI(Resource):
    @marshal_with(assesment_output_fields)
    def get(self,user_id,password):
        id=int(user_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            assesment=db.session.query(Assesment).filter().all()
            unattemped=[]
            attempted=[]
            if assesment:
                # for i in assesment:
                #     aspirant=db.session.query(Aspirant).filter(Aspirant.aspirant_id==id,Aspirant.assesment_id==i.assesment_id)
                #     if aspirant:
                #         attempted.append(aspirant)
                #     else:
                #         unattemped.append(aspirant)
                # print("Attembed")
                # print(attempted)
                # print("Unattempted")
                # print(unattemped)
                return assesment
            else:
                raise NotFoundError(status_code=404)
        else:
            raise NotFoundError(status_code=404)


class AllAspirantsUsersAPI(Resource):
    @marshal_with(aspirant_output_fields)
    def get(self,user_id,password):
        print("IN aspirant")
        id=int(user_id)
        print(id)
        print(password)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            aspirants=db.session.query(Aspirant).filter(Aspirant.aspirant_id==id).all()
            print("Aspirant is")
            print(aspirants)
            if aspirants:
                return aspirants
            else:
                return {},200
        else:
            raise NotFoundError(status_code=404)


class AssesmentAPI(Resource):
    @marshal_with(assesment_output_fields)
    def get(self,user_id,password,assesment_id):
        id=int(user_id)
        id2=int(assesment_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            assesment=db.session.query(Assesment).filter(Assesment.assesment_id==id2).all()
            if assesment:
                return assesment
            else:
                raise NotFoundError(status_code=404)
        else:
            raise NotFoundError(status_code=404)

    def put(self,user_id,password,assesment_id):
        id=int(user_id)
        id2=int(assesment_id)
        args=create_assesment_parser.parse_args()
        Name=args.get('Name',None)
        Descr=args.get("Quiz",None)
        count=args.get("Student_count",None)
        top=args.get("Toppers",None)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        print(user)
        if user:
            tracker=db.session.query(Assesment).filter(Assesment.creator_id==id,Assesment.assesment_id==id2).first()
            if tracker:
                tracker.Name=Name
                tracker.Quiz=Descr
                tracker.Student_count=count
                tracker.Toppers=top
                db.session.commit()
                return {},201
            else:
                raise NotFoundError(status_code=404)         
        else:
            raise NotFoundError(status_code=404)

    def delete(self,user_id,password,assesment_id):
        id=int(user_id)
        id2=int(assesment_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        print(user)
        if user:
            tracker=db.session.query(Assesment).filter(Assesment.assesment_id==id2).first()
            print(tracker)
            if tracker:
                db.session.delete(tracker)
                db.session.commit()
                return {},201
            else:
                raise NotFoundError(status_code=404)

        else:
            raise NotFoundError(status_code=404)

    def post(self,user_id,password):
        id=int(user_id)
        print('tri')
        args=create_assesment_parser.parse_args()
        Descr=args.get("Quiz",None)  
        print("Quiz is")
        print(Descr)
        print(type(Descr))
        Nam=args.get('Name',None)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            new_tracker=Assesment(Name=Nam,Quiz=Descr,creator_id=id,Student_Count =0)
            db.session.add(new_tracker)
            db.session.commit()
            return {},200
        if user_id is None or password is None:
            raise BusinessValidationError(status_code=400,error_code="BE1001",error_message="user_id or password is required")
        else:
            pass
        user=db.session.query(User).filter(User.user_id==int(user_id)).first()
        if user:
            raise BusinessValidationError(status_code=400,error_code="BE1002",error_message="duplicate user_id")



class AspirantAPI(Resource):
    @marshal_with(aspirant_output_fields)
    def get(self,user_id,password,assesment_id):
        id=int(user_id)
        id2=int(assesment_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            aspirant=db.session.query(Aspirant).filter(Aspirant.assesment_id==id2).order_by(Aspirant.aspirant_score.desc()).all()
            if aspirant:
                return aspirant
            else:
                raise NotFoundError(status_code=404)
        else:
            raise NotFoundError(status_code=404)

    def put(self,user_id,password,assesment_id):
        id=int(user_id)
        args=update_aspirant_parser.parse_args()
        id2=int(assesment_id)
        score=args.get('aspirant_score')
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        print(user)
        if user:
            tracker=db.session.query(Aspirant).filter(Aspirant.aspirant_id==id,Aspirant.assesment_id==id2).first()
            if tracker:
                tracker.aspirant_score=score
                db.session.commit()
                return {},201
            else:
                raise NotFoundError(status_code=404)         
        else:
            raise NotFoundError(status_code=404)

    def delete(self,user_id,password,assesment_id):
        id=int(user_id)
        id2=int(assesment_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        print(user)
        if user:
            tracker=db.session.query(Aspirant).filter(Aspirant.aspirant_id==id,Aspirant.assesment_id==id2).first()
            if tracker:
                db.session.delete(tracker)
                db.session.commit()
                asses=db.session.query(Assesment).filter(Assesment.assesment_id==id2).first()
                asses.Student_Count = asses.Student_Count-1
                db.session.commit()
                return {},201
            else:
                raise NotFoundError(status_code=404)
        else:
            raise NotFoundError(status_code=404)

    def post(self,user_id,password,assesment_id):
        id=int(user_id)
        print('tri')
        args=create_aspirant_parser.parse_args()
        score=args.get("aspirant_score")
        na=args.get("aspirant_name")
        print(score)
        id2=int(assesment_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            new_tracker=Aspirant(aspirant_id=id,assesment_id=id2,aspirant_score=score,aspirant_name=na)
            db.session.add(new_tracker)
            db.session.commit()
            asses=db.session.query(Assesment).filter(Assesment.assesment_id==id2).first()
            asses.Student_Count = asses.Student_Count+1
            db.session.commit()
            return {},201
        if user_id is None or password is None:
            raise BusinessValidationError(status_code=400,error_code="BE1001",error_message="user_id or password is required")
        else:
            pass
        user=db.session.query(User).filter(User.user_id==int(user_id)).first()
        if user:
            raise BusinessValidationError(status_code=400,error_code="BE1002",error_message="duplicate user_id")

class ThreadAPI(Resource):
    @marshal_with(thread_output_fields)
    def get(self,user_id,password,thread_id):
        id=int(user_id)
        id2=int(thread_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            tracker=db.session.query(Thread).filter(Thread.thread_id==id2).first()
            if tracker:
                return tracker
            else:
                raise NotFoundError(status_code=404)
        else:
            raise NotFoundError(status_code=404)

    def put(self,user_id,password,thread_id):
        id=int(user_id)
        id2=int(thread_id)
        args=update_thread_parser.parse_args()
        Descr=args.get("Thread_count",None)
        Seet=args.get('Thread_Map',None)    
        Nam=args.get('Title',None)

        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        print(user)
        if user:
            tracker=db.session.query(Thread).filter(Thread.user_id==id,Thread.thread_id==id2).first()
            if tracker:
                tracker.Title=Nam
                tracker.Thread_count=Descr
                tracker.Thread_Map=Seet
                db.session.commit()
                return {},201
            else:
                raise NotFoundError(status_code=404)         
        else:
            raise NotFoundError(status_code=404)

    def delete(self,user_id,password,thread_id):
        id=int(user_id)
        id2=int(thread_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        print(user)
        if user:
            tracker=db.session.query(Thread).filter(Thread.user_id==id,Thread.thread_id==id2).first()
            if tracker:
                db.session.delete(tracker)
                db.session.commit()
                return {},201
            else:
                raise NotFoundError(status_code=404)

        else:
            raise NotFoundError(status_code=404)

    def post(self,user_id,password):
        print("Inside post")
        id=int(user_id)
        print('tri')
        args=create_thread_parser.parse_args()
        Descr=0
        Seet=args.get('Thread_Map',None)    
        Nam=args.get('Title',None)
        print(id)
        print(password)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        
        if user:
            new_thread=Thread(Thread_count=Descr,Thread_Map=Seet,user_id=id,Title=Nam)
            db.session.add(new_thread)
            db.session.commit()
            return {"thread_id":new_thread.thread_id,"status_code":200}
        
        if user_id is None or password is None:
            raise BusinessValidationError(status_code=400,error_code="BE1001",error_message="user_id or password is required")
        else:
            pass
        user=db.session.query(User).filter(User.user_id==int(user_id)).first()
        if user:
            raise BusinessValidationError(status_code=400,error_code="BE1002",error_message="duplicate user_id")


class PostAPI(Resource):
     @marshal_with(post_output_fields)
     def get(self,user_id,password,thread_id,post_id):
        id=int(user_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            id2=int(thread_id)
            tracker=db.session.query(Thread).filter(Thread.user_id==id,Thread.thread_id==id2).first()
            if tracker:
                id3=int(post_id)
                logger=db.session.query(Post).filter(Post.post_id==id3,Post.thread_id==id2).first()
                if logger:
                    return logger
                else:
                    raise NotFoundError(status_code=404)
            else:
                raise NotFoundError(status_code=404)        
        else:
            raise NotFoundError(status_code=404)

     def put(self,user_id,password,thread_id,post_id):
        print("Inside logs")
        id=int(user_id)
        id1=int(thread_id)
        args=update_post_parser.parse_args()
        id2=int(post_id)
        print(id2)
        timeSt=args.get('Annoynmous',"False")
        note=args.get('Post_Message',None)    
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            tracker=db.session.query(Thread).filter(Thread.user_id==id,Thread.thread_id==id1).first()
            if tracker:

                logger=db.session.query(Post).filter(Post.post_id==id2,Post.thread_id==id1).first()
                if logger:
                    logger.Annoynmous=timeSt
                    logger.Post_Message=note
                    india_timezone = pytz.timezone('Asia/Kolkata')
                    current_time_in_india = datetime.now(india_timezone)
                    logger.Post_Date_Time=current_time_in_india
                    db.session.commit()
                    tracker.Thread_Map=current_time_in_india
                    db.session.commit()
            return {},201
        else:
            raise NotFoundError(status_code=404)

     def delete(self,user_id,password,thread_id,post_id):
        id=int(user_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            id2=int(thread_id)
            tracker=db.session.query(Thread).filter(Thread.thread_id==id2).first()
            if tracker:
                id3=int(post_id)
                logger=db.session.query(Post).filter(Post.post_id==id3).first()
                if logger:
                    db.session.delete(logger)
                    db.session.commit()
                    return {},201
                else:
                    raise NotFoundError(status_code=404)
            else:
                raise NotFoundError(status_code=404)        
        else:
            raise NotFoundError(status_code=404)

     def post(self,user_id,password,thread_id):
        print("Inside logs")
        id=int(user_id)
        id1=int(thread_id)
        args=create_post_parser.parse_args()
        timeSt=args.get('Annoynmous',"False")
        note=args.get('Post_Message',None)    
        email=args.get('Poster_email')
        nam=args.get('Poster_Name')

        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            tracker=db.session.query(Thread).filter(Thread.thread_id==id1).first()
            if tracker:
                india_timezone = pytz.timezone('Asia/Kolkata')
                current_time_in_india = datetime.now(india_timezone)
                new_logger=Post(Annoynmous=timeSt,Post_Message=note,thread_id =id1,Post_Date_Time=current_time_in_india,Poster_Name=nam,Poster_email=email)
                db.session.add(new_logger)
                db.session.commit()
                tracker.Thread_Map=current_time_in_india
                if tracker.Thread_count is None:
                    tracker.Thread_count=1
                else:
                    tracker.Thread_count=int(tracker.Thread_count)+1
                db.session.commit()
                return {"message":"su","status_code":200}
            else:
                raise BusinessValidationError(status_code=400,error_code="BE1003",error_message="Tracker_Id is invalid")
        if user_id is None or password is None:
            raise BusinessValidationError(status_code=400,error_code="BE1001",error_message="user_id or password is required")
        else:
            pass
        user=db.session.query(User).filter(User.user_id==int(user_id)).first()
        if user:
            raise BusinessValidationError(status_code=400,error_code="BE1002",error_message="duplicate user_id")


class AllConnectionAPI(Resource):
    @marshal_with(connection_output_fields)
    def get(self,user_id,password):
        id=int(user_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            tracker1=db.session.query(Connection).filter(Connection.receiver_id==id).all()
            if tracker1:
                return tracker1
            else:
                raise NotFoundError(status_code=404)
        else:
            raise NotFoundError(status_code=404)

class AllUsersAPI(Resource):
    @marshal_with(user_output_fields)
    def get(self,user_id,password):
        id=int(user_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        users=db.session.query(User).filter(User.user_id!=id).all()
        if users:
            return users
        else:
            raise NotFoundError(status_code=404)

class ConnectionAPI(Resource):
    @marshal_with(connection_output_fields)
    def get(self,user_id,password,connection_id):
        id=int(user_id)
        id2=int(connection_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            tracker=db.session.query(Connection).filter(Connection.sender_id==id,Connection.connection_id==id2).first()
            tracker1=db.session.query(Connection).filter(Connection.receiver_id==id,Connection.connection_id==id2).first()
            if tracker:
                return tracker
            elif tracker1:
                return tracker1
            else:
                raise NotFoundError(status_code=404)
        else:
            raise NotFoundError(status_code=404)

    def put(self,user_id,password,connection_id):
        id=int(user_id)
        id2=int(connection_id)
        args=update_connection_parser.parse_args()
        Name=args.get('Approval_Status',"Not Responded")
        # Descr=args.get("Connection_Map",None)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            tracker=db.session.query(Connection).filter(Connection.sender_id==id,Connection.connection_id==id2).first()
            tracker1=db.session.query(Connection).filter(Connection.receiver_id==id,Connection.connection_id==id2).first()
            if tracker:
                tracker.Approval_Status=Name
                db.session.commit()
                return {},200
            elif tracker1:
                tracker1.Approval_Status=Name
                db.session.commit()
                if Name=="Accept":
                    print(Name)
                    content=tracker1.Request
                    india_timezone = pytz.timezone('Asia/Kolkata')
                    current_time_in_india = datetime.now(india_timezone)
                    new_logger=Message(Content=content,connection_id =id2,Message_Sender=user.Name,Message_Date_Time=current_time_in_india)
                    db.session.add(new_logger)
                    db.session.commit()
                    tracker1.Connection_Map = current_time_in_india
                    db.session.commit()
                return {},200
            else:
                raise NotFoundError(status_code=404)         
        else:
            raise NotFoundError(status_code=404)

    def delete(self,user_id,password,connection_id):
        id=int(user_id)
        id2=int(connection_id)
        print(id2)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        print(user)
        if user:
            tracker=db.session.query(Connection).filter(Connection.sender_id==id,Connection.connection_id==id2).first()
            tracker1=db.session.query(Connection).filter(Connection.receiver_id==id,Connection.connection_id==id2).first()
            print(tracker1)
            print(tracker)
            if tracker:
                db.session.delete(tracker)
                db.session.commit()
                return {},201
            elif tracker1:
                db.session.delete(tracker1)
                db.session.commit()
                return {},201
            else:
                raise NotFoundError(status_code=404)

        else:
            raise NotFoundError(status_code=404)

    def post(self,user_id,password):
        id=int(user_id)
        print('tri')
        args=create_connection_parser.parse_args()
        receiver_id=int(args.get("receiver_id"))
        print(receiver_id)
        Descr=args.get("Request")
        print("Request Message is ")
        print(Descr)
        sender=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        receiver=db.session.query(User).filter(User.user_id==receiver_id).first()
        if sender and receiver:
            india_timezone = pytz.timezone('Asia/Kolkata')
            current_time_in_india = datetime.now(india_timezone)
            new_tracker=Connection(sender_id=id,receiver_id=receiver_id,Request=Descr,Sender_Name=sender.Name,Receiver_Name=receiver.Name,Connection_Map=current_time_in_india,Approval_Status="Not Responded")
            db.session.add(new_tracker)
            db.session.commit()
            return {},200
        if user_id is None or password is None:
            raise BusinessValidationError(status_code=400,error_code="BE1001",error_message="user_id or password is required")
        else:
            pass
        user=db.session.query(User).filter(User.user_id==int(user_id)).first()
        if user:
            raise BusinessValidationError(status_code=400,error_code="BE1002",error_message="duplicate user_id")

class MessageAPI(Resource):
    @marshal_with(message_output_fields)
    def get(self,user_id,password,connection_id,message_id):
        id=int(user_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            id2=int(connection_id)
            tracker=db.session.query(Connection).filter(Connection.connection_id==id2).first()
            if tracker:
                id3=int(message_id)
                logger=db.session.query(Message).filter(Message.message_id==id3).first()
                if logger:
                    print(logger)
                    return logger
                else:
                    raise NotFoundError(status_code=404)
            else:
                raise NotFoundError(status_code=404)        
        else:
            raise NotFoundError(status_code=404)

    def put(self,user_id,password,connection_id,message_id):
        id=int(user_id)
        id1=int(connection_id)
        id2=int(message_id)
        args=update_message_parser.parse_args()
        timeSt=args.get('Content',None)   
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            tracker=db.session.query(Connection).filter(Connection.connection_id==id1).first()
            if tracker:
                logger=db.session.query(Message).filter(Message.message_id==id2,Message.connection_id==id1).first()
                if logger:
                    logger.Content=timeSt
                    db.session.commit()
            return {},201
        else:
            raise NotFoundError(status_code=404)

    def delete(self,user_id,password,connection_id,message_id):
        id=int(user_id)
        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            id2=int(connection_id)
            tracker=db.session.query(Connection).filter(Connection.connection_id==id2).first()
            if tracker:
                id3=int(message_id)
                logger=db.session.query(Message).filter(Message.connection_id==id3,Message.message_id==id2).first()
                if logger:
                    db.session.delete(logger)
                    db.session.commit()
                    return {},201
                else:
                    raise NotFoundError(status_code=404)
            else:
                raise NotFoundError(status_code=404)        
        else:
            raise NotFoundError(status_code=404)

    def post(self,user_id,password,connection_id):
        print("Inside logs")
        id=int(user_id)
        id1=int(connection_id)
        args=create_message_parser.parse_args()
        timeSt=args.get('Content',None)
        sender=args.get('Message_Sender')

        user=db.session.query(User).filter(User.user_id==id,User.password==password).first()
        if user:
            tracker=db.session.query(Connection).filter(Connection.connection_id==id1).first()
            if tracker:
                india_timezone = pytz.timezone('Asia/Kolkata')
                current_time_in_india = datetime.now(india_timezone)
                new_logger=Message(Content=timeSt,connection_id =id1,Message_Sender=sender,Message_Date_Time=current_time_in_india)
                db.session.add(new_logger)
                db.session.commit()
                tracker.Connection_Map=current_time_in_india
                db.session.commit()
                return {"message":"su","status_code":200}
            else:
                raise BusinessValidationError(status_code=400,error_code="BE1003",error_message="Tracker_Id is invalid")
        if user_id is None or password is None:
            raise BusinessValidationError(status_code=400,error_code="BE1001",error_message="user_id or password is required")
        else:
            pass
        user=db.session.query(User).filter(User.user_id==int(user_id)).first()
        if user:
            raise BusinessValidationError(status_code=400,error_code="BE1002",error_message="duplicate user_id")

