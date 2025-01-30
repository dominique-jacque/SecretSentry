# SecretSentry

## Overview

The Secret Sharing App is a security-focused platform that enables users to share sensitive information by storing it in an Amazon S3 bucket. A generated link allows recipients to access the secret for a limited duration of three days. The application incorporates AWS security best practices to ensure confidentiality and controlled access.

## Architecture

The project is built using AWS services with a security-first approach:

- IAM Policies (Access Control): Separate policies govern access to secrets and the data citadel, ensuring role-based permissions.

- S3 Configuration:

- Secrets Vault: Fortified with strict policies, versioning, and encryption to ensure maximum security.

- Data Citadel: Protected with encryption and controlled access.
 
- KMS Integration: AWS Key Management Service (KMS) is used for additional encryption to secure sensitive data.

- Lambda Functions (Security Operations): Handle secret-related operations such as encryption, decryption, and access control.

- API Gateway (Sentry Communication): Provides secure endpoints that connect to Lambda functions for secret management.

- CloudWatch (Surveillance Ops): Enables monitoring and logging to track access and potential security incidents.

## Features

- Neat and intuitive UI/UX design, ensuring a seamless and engaging user experience.

- Secure storage of sensitive information in an encrypted S3 bucket.

- Temporary access link valid for 3 days.

- Fine-grained access control with IAM policies.

- Automated encryption and decryption of secrets using AWS KMS.

- Logging and monitoring for security oversight.

## Security Considerations

- IAM Role Separation: Ensuring least privilege access.

- Encryption at Rest and in Transit: Using S3 and API Gateway encryption features.

- AWS KMS for Key Management: Ensures secure handling of encryption keys.

- Logging and Monitoring: CloudWatch provides activity tracking.

- Expiration Policies: Secrets expire after 3 days to reduce exposure risk.

## Future Enhancements

- Docker Containerization: Deploy components in Docker containers.

- Multi-Factor Authentication (MFA): Enhance access security.

- Temporary Secret Revocation: Allow manual expiration before 3 days.

- EKS or ECS Deployment: Explore Kubernetes or container orchestration.