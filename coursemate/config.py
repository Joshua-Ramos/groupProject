class DevConfig:
    DEVELOPTMENT = True

    # AWS S3
    S3_KEY = 'AKIAJZ6GXZRQMZIAADIA'
    S3_SECRET = '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'
    S3_BUCKET = 'coursemat' # typo?
    S3_UPLOAD_DIRECTORY = 'Testing'
    SECRET_KEY = 'TestingSecretKey'

    # SQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Jahag@123@localhost/CourseMate'