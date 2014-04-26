from storages.backends.s3boto import S3BotoStorage

StaticS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaS3BotoStorage = lambda: S3BotoStorage(location='media')

import math


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)