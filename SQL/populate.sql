INSERT INTO User(First_Name, Last_Name, Username, Password, Email, Photo_Location)
            VALUES("Amogh", "Jahagirdar", "AmoghUsername", "BcryptedAmoghPassword", "Amogh.Jahagirdar@Colorado.edu", "HashedAmoghPhotoLocationAWS");

INSERT INTO User(First_Name, Last_Name, Username, Password, Email, Photo_Location)
            VALUES("Joshua", "Ramos", "JoshuaUsername", "BcryptedJoshuaPassword", "Joshua.Ramos@Colorado.edu", "HashedJoshuaPhotoLocationAWS");

INSERT INTO User(First_Name, Last_Name, Username, Password, Email, Photo_Location)
            VALUES("Elliott", "Shugerman", "ElliottUsername", "BcryptedElliottPassword", "Elliott.Shugerman@Colorado.edu", "HashedElliottPhotoLocationAWS");

INSERT INTO User(First_Name, Last_Name, Username, Password, Email, Photo_Location)
            VALUES("Alexander", "Fisher", "AlexanderUsername", "BcryptedAlexanderPassword", "Alexander.M.Fisher@Colorado.edu", "HashedAlexanderPhotoLocationAWS");

INSERT INTO User(First_Name, Last_Name, Username, Password, Email, Photo_Location)
            VALUES("Ruben", "Vargas", "RubenUsername", "BcryptedRubenPassword", "Ruben.Vargas@Colorado.edu", "HashedRubenPhotoLocationAWS");

INSERT INTO User(First_Name, Last_Name, Username, Password, Email, Photo_Location)
            VALUES("ad", "min", "admin", "password", "ad@min.edu", "HashedRubenPhotoLocationAWS");




INSERT INTO File(Location, File_Name, User_ID, Uploaded, File_ID)
            VALUES("practiceExam1location", "practiceExam1.pdf", 2, "2017-02-05", 1);

INSERT INTO File(Location, File_Name, User_ID, Uploaded, File_ID)
            VALUES("practiceExam2location", "practiceExam2.pdf", 4, "2017-02-07", 2);

INSERT INTO File(Location, File_Name, User_ID, Uploaded, File_ID)
            VALUES("practiceExam3location", "practiceExam3.pdf", 5, "2017-02-09", 3);

INSERT INTO File(Location, File_Name, User_ID, Uploaded, File_ID)
            VALUES("AlgorithmsNotes1Location", "AlgoNotes.ppt", 1, "2017-02-08", 4);

INSERT INTO File(Location, File_Name, User_ID, Uploaded, File_ID)
            VALUES("SoftwareDevNotes1Location", "SoftwareNotes.txt", 3, "2017-03-10", 5);



INSERT INTO Class(Class_Name, Class_ID, Instructor_First, Instructor_Last, CA_First, CA_Last)
            VALUES("Software Development and Tools", 3308, "Alan", "Paradise", "Yogitha", "Mahadasu");

INSERT INTO Class(Class_Name, Class_ID, Instructor_First, Instructor_Last, CA_First, CA_Last)
            VALUES("Statistical Methods", 4570, "Yolanda", "Slichter", "Amogh", "Jahagirdar");

INSERT INTO Class(Class_Name, Class_ID, Instructor_First, Instructor_Last, CA_First, CA_Last)
            VALUES("Algorithms", 3104, "Aaron", "Clauset", "Cormen", "Leirson");

INSERT INTO Class(Class_Name, Class_ID, Instructor_First, Instructor_Last, CA_First, CA_Last)
            VALUES("Discrete Structures", 2824, "Mike", "Eisenberg", "George", "Polya");




INSERT INTO Post(Post_Name, File_ID, User_ID, Class_ID, Time, Post_Text)
            VALUES("Practice Exam 1 for Discrete Structures",1,1,2824,"2017-02-06", "Attached is the 1st Practice Exam for Discrete Structures");

INSERT INTO Post(Post_Name, File_ID, User_ID, Class_ID, Time, Post_Text)
            VALUES("Practice Exam 2 for Algorithms",2,3,3104, "2017-02-08", "Attached is the 2nd Practice Exam for Algorthms");

INSERT INTO Post(Post_Name, File_ID, User_ID, Class_ID, Time, Post_Text)
            VALUES("Practice Exam 3 for Statistical Methods",3,4,4570, "2017-02-10", "Attached is the 3rd Practice Exam for Statistical Methods");

INSERT INTO Post(Post_Name, File_ID, User_ID, Class_ID, Time, Post_Text)
            VALUES("Updated Software Development Notes",5,5,3308, "2017-03-11", "Attached is the updated Software Dev notes");
