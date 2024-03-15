#1 Challenge: Provisioning a 3-tier environment on AWS using Terraform
# main.tf
# Modularization is the key !

# Provider configuration - AWS 
provider "aws" {
  region = "us-east-1"
}

# Creating a VPC for isolation purpose
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

# Creating a public subnet
resource "aws_subnet" "public" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.1.0/24"
  map_public_ip_on_launch = true
}

# Creating a private subnet
resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.2.0/24"
}

# Creating security groups for web, app, and database tiers
resource "aws_security_group" "web_sg" {
  vpc_id = aws_vpc.main.id
  # Define security group rules as needed
}

resource "aws_security_group" "app_sg" {
  vpc_id = aws_vpc.main.id
  # Define security group rules as needed
}

resource "aws_security_group" "db_sg" {
  vpc_id = aws_vpc.main.id
  # Define security group rules as needed
}

# We Can also provide Additional resources (e.g., CodeCommit for repo, EC2 instances, RDS, ELB, etc.) can be provisioned as per the requirement
