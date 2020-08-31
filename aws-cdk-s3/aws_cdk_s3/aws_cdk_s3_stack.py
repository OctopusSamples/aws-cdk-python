from aws_cdk import core, aws_s3


class AwsCdkS3Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = aws_s3.Bucket(
                    self,
                    "mjls3Bucket1992323",
                    public_read_access=True
                )
        bucket