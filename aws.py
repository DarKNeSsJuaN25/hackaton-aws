# Compute
from diagrams.aws.compute import (
  EC2, Lambda, ECS, Fargate, Batch, Lightsail
)

# Networking
from diagrams.aws.network import (
  ELB, ALB, NLB, VPC, Route53, CloudFront, InternetGateway, APIGateway
)

# Storage
from diagrams.aws.storage import (
  S3, EBS, EFS, StorageGateway, S3Glacier, S3AccessPoints,
  ElasticBlockStoreEBS, ElasticBlockStoreEBSSnapshot,
  ElasticFileSystemEFS, Fsx, Snowball, Backup
)

# Database
from diagrams.aws.database import (
  RDS, Redshift, ElastiCache
)

# Analytics
from diagrams.aws.analytics import (
  Athena, Glue, GlueDataCatalog, GlueCrawlers, Kinesis,
  KinesisDataStreams, KinesisDataFirehose, KinesisDataAnalytics,
  AmazonOpensearchService, DataPipeline, LakeFormation
)

# Security
from diagrams.aws.security import (
  IAM, Cognito, CertificateManager, Inspector, WAF
)

node_types = {
  # Compute
  "EC2": EC2,
  "Lambda": Lambda,
  "ECS": ECS,
  "Fargate": Fargate,
  "Batch": Batch,
  "Lightsail": Lightsail,

  # Networking
  "ELB": ELB,
  "ALB": ALB,
  "NLB": NLB,
  "VPC": VPC,
  "Route53": Route53,
  "CloudFront": CloudFront,
  "InternetGateway": InternetGateway,
  "APIGateway": APIGateway,

  # Storage
  "S3": S3,
  "S3Glacier": S3Glacier,
  "S3AccessPoints": S3AccessPoints,
  "EBS": ElasticBlockStoreEBS,
  "EBSSnapshot": ElasticBlockStoreEBSSnapshot,
  "EFS": ElasticFileSystemEFS,
  "FSx": Fsx,
  "Snowball": Snowball,
  "StorageGateway": StorageGateway,
  "Backup": Backup,

  # Database
  "RDS": RDS,
  "Redshift": Redshift,
  "ElastiCache": ElastiCache,

  # Analytics
  "Athena": Athena,
  "Glue": Glue,
  "GlueDataCatalog": GlueDataCatalog,
  "GlueCrawlers": GlueCrawlers,
  "Kinesis": Kinesis,
  "KinesisDataStreams": KinesisDataStreams,
  "KinesisDataFirehose": KinesisDataFirehose,
  "KinesisDataAnalytics": KinesisDataAnalytics,
  "Redshift": Redshift,
  "Opensearch": AmazonOpensearchService,
  "DataPipeline": DataPipeline,
  "LakeFormation": LakeFormation,

  # Security
  "IAM": IAM,
  "Cognito": Cognito,
  "CertificateManager": CertificateManager,
  "Inspector": Inspector,
  "WAF": WAF,
}

