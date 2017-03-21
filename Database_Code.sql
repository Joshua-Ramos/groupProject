/*
Creating database and tables
*/

Create database Coursemate;
CREATE TABLE User (First_Name VARCHAR(35), Last_Name VARCHAR(35), Username VARCHAR(16), Password VARCHAR(50), Email VARCHAR(254), Photo_Location VARCHAR(100), User_ID INTEGER, PRIMARY KEY(Username, Password));
CREATE TABLE File(Location VARCHAR(100), File_Name VARCHAR(150), User_ID INTEGER, Uploaded DATE, File_ID INTEGER, PRIMARY KEY(FILE_ID));
CREATE TABLE Class(Class_Name VARCHAR(150), Class_ID INTEGER, Instructor_First VARCHAR(35), Instructor_Last VARCHAR(35), CA_First VARCHAR(35), CA_Last VARCHAR(35), PRIMARY KEY(Class_ID, CA_First, CA_Last));
CREATE TABLE Post(Post_Name VARCHAR(150), File_ID INTEGER, User_ID INTEGER, Class_ID INTEGER, Time DATE, Post_Text VARCHAR(MAX), PRIMARY KEY(Post_name, File_ID, Class_ID, Time, User_ID));
