class DevConfig:
    DEVELOPTMENT = True

    # AWS S3
    ##NOTE PLEASE INSERT THE KEY AND SECRET BEFORE RUNNING
    S3_KEY = ''
    S3_SECRET = ''

    S3_BUCKET = 'coursemat' # typo?
    S3_UPLOAD_DIRECTORY = 'Testing'
    SECRET_KEY = 'TestingSecretKey'

    # SQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://CourseMate:password@localhost/CourseMate'
