##This Python helper file contains "filters" for basic queries that will be performed##
from .models import User, Course, Post, File, db

def valid_course(course_id):
    return Course.query.filter_by(class_id = course_id).first() is not None
