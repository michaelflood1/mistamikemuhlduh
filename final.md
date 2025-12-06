# Final Exam Study Sheet
## Enterprise Development Environment

---

## Table of Contents
1. [Enterprise Development Environment Overview](#enterprise-development-environment-overview)
2. [Tools and Their Capabilities](#tools-and-their-capabilities)
3. [DevOps Concepts - CI/CD](#devops-concepts---cicd)
4. [Jenkinsfile and Shared Libraries](#jenkinsfile-and-shared-libraries)
5. [Jenkins vs GitLab CI](#jenkins-vs-gitlab-ci)
6. [On-Premise vs Cloud](#on-premise-vs-cloud)
7. [Development Workflows](#development-workflows)
8. [Tool Assessment - Stakeholder Perspectives](#tool-assessment---stakeholder-perspectives)
9. [Improvements to Enterprise Development Environment](#improvements-to-enterprise-development-environment)
10. [Key Review Topics](#key-review-topics)

---

## Enterprise Development Environment Overview

### What is an Enterprise System?
- A **large-scale organization** requiring complex, integrated systems
- Systems used **organization-wide** (not individual tools)
- Examples: CRM, HR systems, time tracking, ERP
- Typically has **multiple users and stakeholders**
- Requires **complex integration** between different systems

### What is Enterprise System Integration?
- **Connecting different enterprise systems** to work together
- Enables data sharing and process automation across systems
- **Improves efficiency** by reducing manual work and duplication
- Creates a **unified ecosystem** of tools and processes
- Allows systems to communicate and share information

### What is an Enterprise Development Environment?
A complete, integrated set of tools and systems that support the entire software development lifecycle.

**Key Components We Covered:**

1. **Source Code Management (SCM)**
   - Tool: GitLab
   - Version control for code, schemas, scripts

2. **Continuous Integration/Continuous Delivery (CI/CD)**
   - Tool: Jenkins
   - Automated build, test, deploy pipelines

3. **Static Code Analysis**
   - Tool: SonarQube
   - Code quality, security vulnerabilities, technical debt tracking

4. **Artifact Management**
   - Tool: Nexus
   - Version-controlled storage for build artifacts

5. **Work Management**
   - Tool: JIRA
   - Task tracking, project management, agile workflows

6. **Knowledge Base**
   - Tool: Confluence
   - Documentation, collaboration, information sharing

### Why Have an Enterprise Development Environment?
- **Improved Efficiency**: Automation reduces manual work
- **Better Quality**: Automated testing and code analysis
- **Consistency**: Standardized processes across teams
- **Collaboration**: Integrated tools enable better teamwork
- **Traceability**: Audit trails and version control
- **Faster Time to Market**: Automated CI/CD pipelines
- **Risk Reduction**: Automated testing catches issues early

### Relationship Between Enterprise System Integration and EDE
- Enterprise Development Environment **IS** an example of enterprise system integration
- Integrates development tools to create seamless workflows
- Tools communicate with each other (e.g., Jenkins pulls from GitLab, posts to JIRA)
- Single sign-on (SSO) can integrate authentication across tools
- Webhooks and APIs enable tool integration

---

## Tools and Their Capabilities

### GitLab
**Capability**: Source Code Management (SCM)
- Version control (Git-based)
- Repository hosting
- Merge/Pull requests
- Code review
- Branch management
- Can also do CI/CD (GitLab CI)

### Jenkins
**Capability**: Continuous Integration/Continuous Delivery Pipelines
- Automated build execution
- Pipeline orchestration
- Controller-Agent architecture
- Plugin ecosystem
- Pipeline as Code (Jenkinsfile)
- Supports parallel execution
- Shared libraries for reusable code

### SonarQube
**Capability**: Static Code Analysis
- **Four Main Components**:
  1. Server (web interface, compute engine)
  2. Scanners (analyze source code)
  3. Plugins (language support, integrations)
  4. Database (stores configuration and snapshots)

- **Issue Types Tracked**:
  - Vulnerabilities (security issues)
  - Code Smells (maintainability issues)
  - Bugs (potential defects)

- **Key Features**:
  - Technical Debt calculation
  - Quality Gates
  - Snapshots (measures at a point in time)
  - SonarLint (IDE integration - should be used FIRST)

### Nexus
**Capability**: Artifact Management
- Version-controlled artifact storage
- Artifact sharing across teams
- Proxy for external repositories
- Support for multiple formats (Maven, npm, Docker, etc.)
- **Advantages over file system**: Versioning and centralized management

### JIRA
**Capability**: Work Management
- Issue/task tracking
- Agile board management (Scrum, Kanban)
- Sprint planning
- Project management
- Workflow customization
- Integration with other tools

### Confluence
**Capability**: Knowledge Base
- Documentation repository
- Team collaboration
- Page hierarchies
- Code snippet support
- Search capabilities
- Integration with JIRA

---

## DevOps Concepts - CI/CD

### Three Primary Practice Areas of DevOps
1. **Continuous Delivery**
   - Automated build, test, deploy processes
   - Fast, reliable releases
   - Reduces manual intervention

2. **Infrastructure Automation**
   - Infrastructure as Code (IaC)
   - OS configs and app deployments as code
   - Stored in source code management
   - Repeatable, version-controlled infrastructure

3. **Site Reliability Engineering (SRE)**
   - Operating and monitoring systems
   - Orchestration
   - Designing for operability
   - Reliability and uptime

### Continuous Integration (CI) Best Practices

**What Should Go in Your Repository:**
- Source code
- Database schemas
- Install scripts
- Test scripts
- Jenkinsfile/pipeline definitions
- **NOT**: Compiled binaries, OS files

**CI Server Characteristics:**
- Build runs **automatically on every code change**
- Fast builds (quick feedback)
- Automated testing
- Visibility of build status
- Runs on every checkin to repository

**Key Principles:**
- Commit frequently to mainline
- When build breaks, **fixing it is top priority** (but not everyone drops everything)
- Helps detect conflicts between developers quickly
- Provides fast feedback

### Continuous Testing
- Running tests **continually throughout the delivery process**
- Not just unit tests
- Not just manual testing
- Automated and integrated into pipeline

### Benefits of Continuous Delivery
1. **Low risk releases**
2. **Higher quality**
3. **Lower costs**

---

## Jenkinsfile and Shared Libraries

### Jenkinsfile

**What is it?**
- Text file that defines a Jenkins pipeline
- Written in Groovy DSL
- Stored in source control with the code

**Why is it Good?**
- **Single source of truth** for the pipeline
- **Audit trail** - version controlled changes
- **Code review** - pipeline changes can be reviewed
- **Enables automation** - can automatically create pipelines for branches/PRs
- Supports iteration and improvement
- Declarative or Scripted syntax

**Structure of Declarative Pipeline:**
```groovy
pipeline {
    agent { ... }  // WHERE to execute (required)
    
    stages {
        stage('Build') {
            steps {
                // Individual tasks
            }
        }
        stage('Test') {
            steps { ... }
        }
        stage('Deploy') {
            steps { ... }
        }
    }
}
```

**Key Components:**
- **Pipeline block**: Top-level container
- **Agent**: Specifies WHERE pipeline/stage executes (required)
- **Stages**: Conceptually distinct phases (Build, Test, Deploy)
- **Steps**: Individual tasks (sh 'make', etc.)

**Pipeline Triggering:**
- **Best practice**: Triggered by **change to source code**
- Can also: scheduled, manual (but not preferred)

**Best Practice:**
- Store Jenkinsfile **in source control**, NOT in Jenkins job definition

### Shared Libraries

**What is a Shared Library?**
- Reusable pipeline code shared across projects
- Reduces redundancy (DRY principle)
- Written in **Groovy**
- Centralized, version-controlled

**Three Components of a Shared Library:**
1. **Name**
2. **Version** (optional - can use default)
3. **Source Code Retrieval Method** (Git repo URL)

**Repository Structure:**
- `/src` - Groovy source files
- `/vars` - Script files exposed as variables
- `/resources` - Non-Groovy files

**Why Use Shared Libraries?**
- **Enable code reuse** across multiple projects
- Maintain consistency
- Centralized updates
- Reduce duplication

**How to Use:**
```groovy
@Library('my-shared-library') _
evenOrOdd(currentBuild.getNumber())
```

**Global vs Folder Libraries:**
- **Global**: Available to ALL pipeline jobs (defined in Jenkins config)
- **Folder**: Available to specific pipelines

**Development Tools:**
- Command-Line Pipeline Linter
- Blue Ocean Editor
- IDE Plugins (Eclipse, VS Code, etc.)
- Replay Pipeline Runs with Modifications

---

## Jenkins vs GitLab CI

### Similarities
- Both provide CI/CD capabilities
- Both use YAML/code-based pipeline definitions
- Both support automated builds, tests, deployments
- Both integrate with source control
- Both support parallel execution
- Both have web interfaces
- Both can run on-premise or cloud

### Differences

| Aspect | Jenkins | GitLab CI |
|--------|---------|-----------|
| **Architecture** | Controller-Agent (separate components) | Integrated with GitLab (GitLab Server + Runners) |
| **Pipeline Definition** | Jenkinsfile (Groovy) | .gitlab-ci.yml (YAML) |
| **Installation** | Standalone tool | Part of GitLab platform |
| **Flexibility** | Highly extensible with plugins | More opinionated, integrated |
| **Configuration** | More complex, more options | Simpler, streamlined |
| **Integration** | Requires separate SCM integration | Native integration with GitLab repos |
| **Runners vs Agents** | Agents (managed by Controller) | Runners (registered with GitLab) |

### Jenkins Architecture Components
1. **Controller**: Web server, "brains" of the system
2. **Agent/Node**: Runs pipeline stages (Java-based, cross-platform)
3. **Executor**: Manages task execution on a node
4. **Builtin Node**: Controller's built-in execution capability

**Why Use Separate Agents?**
- **Scalability**: Distribute workload
- **Cross-Platform Support**: Different OS/environments

### GitLab CI Architecture Components
1. **GitLab Server**: Source code management + CI/CD orchestration
2. **GitLab Runners**: Execute jobs (similar to Jenkins agents)
3. **.gitlab-ci.yml**: Pipeline definition file

### Communication and Authentication

**Jenkins:**
- Controller and Agents communicate via SSH or JNLP
- Authentication: API tokens, SSH keys
- Webhooks from GitLab trigger builds
- GitLab integration plugin

**GitLab CI:**
- GitLab Server communicates with Runners via API
- Runners register with GitLab using registration tokens
- Authentication: Runner tokens, API tokens
- Native integration (no plugins needed)

### When to Use Which?

**Use Jenkins when:**
- Need maximum flexibility and customization
- Already have Jenkins infrastructure
- Complex, multi-tool integrations required
- Need extensive plugin ecosystem
- Using non-GitLab SCM

**Use GitLab CI when:**
- Using GitLab for source control
- Want simpler, integrated solution
- Prefer YAML-based configuration
- Want native SCM integration
- Starting fresh with CI/CD

### Personal Preference Considerations
- **Jenkins**: More powerful, more complex, steeper learning curve
- **GitLab CI**: Simpler, integrated, faster to set up
- Choose based on: existing tools, team expertise, requirements

---

## On-Premise vs Cloud

### On-Premise Infrastructure

**Characteristics:**
- **Controlled by your organization**
- **Capital Expense** (CapEx)
- **Pay upfront** for hardware/software
- Physical servers in your data center
- You manage everything (hardware, OS, updates, security)
- **Fixed capacity**

**Advantages:**
- Complete control over infrastructure
- Data sovereignty (data stays on-site)
- Meets strict regulatory requirements
- No recurring cloud costs
- Customizable to exact specifications

**Disadvantages:**
- High upfront costs
- Requires IT staff to maintain
- Scaling requires hardware purchases
- Longer deployment times
- You manage all updates and security

### Cloud Infrastructure

**Characteristics:**
- **Controlled by 3rd party** (AWS, Azure, GCP)
- **Operational Expense** (OpEx)
- **Pay-as-you-go** model
- Virtual resources, no physical hardware
- Provider manages infrastructure
- **Scalable on demand**

**Advantages:**
- Low upfront costs
- Scale quickly (up or down)
- No hardware maintenance
- Instant deployment
- Global availability
- Managed services available

**Disadvantages:**
- Ongoing subscription costs
- Less control
- Data stored off-site
- Potential vendor lock-in
- May not meet certain compliance requirements

### IaaS vs SaaS

**IaaS (Infrastructure as a Service):**
- Provides infrastructure resources (compute, storage, networking)
- Examples: AWS EC2, Azure Virtual Machines, Google Compute Engine
- You manage: OS, applications, data
- Provider manages: hardware, virtualization, networking

**SaaS (Software as a Service):**
- Provides complete applications
- Examples: Salesforce, Office 365, Gmail
- You manage: data, users
- Provider manages: everything else (infrastructure, platform, application)

### When to Use On-Premise vs Cloud

**Choose On-Premise when:**
- **Strict regulatory requirements** for data sovereignty
- Sensitive data (trade secrets, classified information)
- Existing infrastructure investment
- Specific security requirements
- Predictable, consistent workloads
- Long-term cost optimization (if large scale)

**Choose Cloud when:**
- **Small company with limited IT resources**
- Need rapid scalability
- Variable/unpredictable workloads
- Want to minimize upfront investment
- Need global distribution
- Prefer operational expense model
- Want managed services

**Choose Hybrid (Both) when:**
- Some workloads on-premise (sensitive data)
- Some workloads in cloud (scalable services)
- Gradual cloud migration
- Disaster recovery/backup

---

## Development Workflows

### Trunk-Based Development

**Concept:**
- All developers commit to a single branch (trunk/main/master)
- Very short-lived feature branches (hours to a day)
- Frequent integration to trunk
- Continuous integration is critical

**Advantages:**
- Simpler branching model
- Faster integration
- Encourages small, incremental changes
- Reduces merge conflicts
- Enables continuous delivery

**Disadvantages:**
- Requires discipline
- Needs strong automated testing
- Feature flags may be needed for incomplete features

### Feature Branching

**Concept:**
- Each feature developed in its own branch
- Branch lives until feature is complete
- Merged back to main via pull/merge request
- Branches can be long-lived

**Advantages:**
- Isolated feature development
- Easy to abandon incomplete features
- Code review before merge
- Parallel feature development

**Disadvantages:**
- Can lead to merge conflicts
- Integration delayed until merge
- "Integration hell" if branches live too long
- Slower feedback

### GitFlow

**Concept:**
- Structured branching model with specific branch types
- **Branches:**
  - `main/master` - production-ready code
  - `develop` - integration branch
  - `feature/*` - new features
  - `release/*` - release preparation
  - `hotfix/*` - production fixes

**Advantages:**
- Clear structure
- Supports multiple versions
- Organized release process

**Disadvantages:**
- Complex
- More overhead
- Can slow down delivery
- Not ideal for continuous deployment

### Merge/Pull Requests

**Purpose:**
- Code review mechanism
- Discussion before integration
- Quality gate
- Knowledge sharing

**Best Practices:**
- Keep PRs small and focused
- Require reviews before merge
- Automated tests must pass
- Clear description of changes

### Forking Workflow

**Concept:**
- Each developer has their own server-side copy (fork)
- Changes made in fork
- Pull request to original repo
- Common in open source

**Advantages:**
- No direct commit access needed to main repo
- Maintainers control what gets merged
- Clear separation of contributions

---

## Tool Assessment - Stakeholder Perspectives

### Stakeholders in Enterprise Development Environment

1. **Software Developers**
2. **Project Manager/Team Lead**
3. **IT Operations/Administration**
4. **End Users** (sometimes)

### Assessment Framework: Functional vs Non-Functional Requirements

**Functional Requirements:**
- Define **what a system does**
- Specific features and capabilities
- Examples:
  - "System sends email notification when order completes"
  - "System allows users to enter and track orders"
  - "System generates monthly financial report"

**Non-Functional Requirements (NFRs):**
- Define **how well the system does it**
- Also called: "ilities", Quality Attributes, Architecturally Significant Requirements
- Constraints on design/implementation

**Categories of NFRs:**
1. **Security**
2. **Scalability**
3. **Availability**
4. **Usability**
5. **Testability**
6. **Maintainability**
7. **Performance**
8. **Compatibility**

**Examples of NFRs:**
- "System must work on Chrome, Firefox, and Safari" (Compatibility)
- "System must handle 2 million concurrent users" (Scalability/Performance)
- "System must be restored within 8 hours" (Availability)
- "All PII must be encrypted" (Security)

### What Each Stakeholder Cares About

#### Software Developers

**Functional Requirements:**
- Search capabilities
- Code snippet support
- Syntax highlighting
- API/CLI access
- IDE integration
- Branching and merging features
- Ability to review commit history
- Debugging tools

**Non-Functional Requirements:**
- **Usability**: Intuitive UI, easy to navigate
- **Performance**: Fast response times
- **Compatibility**: Works with their IDE/tools
- **Maintainability**: Easy to update/configure
- Easy integration with existing tools
- Good documentation

**For Different Tools:**
- **SCM (GitLab)**: Branching, merging, code review, IDE integration
- **CI/CD (Jenkins)**: Easy pipeline creation, debugging, logs
- **Knowledge Base (Confluence)**: Search, code snippets, easy editing
- **Static Analysis (SonarQube)**: IDE integration (SonarLint), clear reports

#### Project Manager/Team Lead

**Functional Requirements:**
- Reporting capabilities
- Dashboard/visibility
- User management
- Project tracking
- Budget tracking
- Resource allocation

**Non-Functional Requirements:**
- **Usability**: Easy for team to adopt
- **Cost**: Licensing, per-user pricing
- **Scalability**: Can grow with team
- **Integration**: Works with other tools
- **Training**: Easy to learn
- Vendor support and reliability

**Specific Concerns:**
- Team productivity
- Project visibility
- ROI (return on investment)
- Time to value

#### IT Operations/Administration

**Functional Requirements:**
- Backup and restore
- User management
- Monitoring and alerting
- Log management
- Configuration options

**Non-Functional Requirements:**
- **Ease of installation and maintenance**
- **Security**: Authentication, authorization, encryption
- **Availability**: Uptime, disaster recovery
- **Scalability**: Handle growing users/data
- **Support**: Vendor support for troubleshooting
- On-premise deployment capability (if needed)
- Documentation for operations

**Specific Concerns:**
- System reliability
- Security compliance
- Backup/recovery procedures
- Maintenance windows
- Update/upgrade process
- Hardware/infrastructure requirements

### Sample Tool Assessment Scenario

**Scenario**: Assessing a Knowledge Base tool (like Confluence)

**Developers want:**
- ✓ Code snippet support
- ✓ Markdown/formatting options
- ✓ Good search functionality
- ✓ Integration with JIRA/development tools
- ✓ Easy to create and edit pages

**Project Manager wants:**
- ✓ Dashboard showing documentation coverage
- ✓ Reasonable cost per user
- ✓ Reporting on page views/usage
- ✓ Permission management
- ✓ Easy team onboarding

**IT Operations wants:**
- ✓ On-premise or cloud deployment options
- ✓ SSO integration
- ✓ Backup and restore capabilities
- ✓ Security features (encryption, access control)
- ✓ Vendor support availability
- ✓ Easy maintenance and updates

### Sample Tool Assessment: Source Code Management

**Developers:**
- Branching and merging features
- Code review capabilities
- IDE integration
- Fast operations
- Good documentation

**Operations:**
- Easy installation and maintenance ✓
- Ability to contact support ✓
- Backup and disaster recovery
- Security features
- User authentication options

**NOT Important to Operations:**
- UI for browsing (developer concern)
- IDE integration (developer concern)
- Developer performance metrics (not appropriate use)

---

## Improvements to Enterprise Development Environment

### Security Improvements

**Current Gaps to Address:**
- Individual passwords for each tool → **Implement SSO (Single Sign-On)**
- Basic authentication → **Add Multi-Factor Authentication (MFA)**
- No role-based access → **Implement RBAC (Role-Based Access Control)**
- Unencrypted communications → **Enforce HTTPS/TLS everywhere**
- Secrets in code → **Use secrets management (HashiCorp Vault, AWS Secrets Manager)**
- No audit logging → **Implement centralized audit logging**

**Specific Improvements:**
1. **Single Sign-On (SSO)**
   - LDAP/Active Directory integration
   - SAML or OAuth integration
   - Reduces password fatigue
   - Centralized user management

2. **Multi-Factor Authentication**
   - Add second factor (SMS, app, hardware token)
   - Protects against password compromise

3. **Role-Based Access Control (RBAC)**
   - Granular permissions
   - Principle of least privilege
   - Separate roles: developer, admin, viewer

4. **Secrets Management**
   - No hardcoded passwords
   - Encrypted storage
   - Automatic rotation
   - Audit trail for secret access

5. **Network Security**
   - Firewalls
   - VPN access for remote users
   - Network segmentation

6. **Container Security**
   - Scan container images for vulnerabilities
   - Use minimal base images
   - Don't run containers as root

### Usability Improvements

**Current Gaps:**
- Multiple logins required → **SSO**
- Complex interfaces → **Standardize UI/UX**
- No unified dashboard → **Create central dashboard**
- Difficult navigation between tools → **Integration and linking**

**Specific Improvements:**
1. **Single Sign-On** (security AND usability)
2. **Unified Dashboard**
   - Show status of all tools in one place
   - Quick links to common tasks
   - Personalized views

3. **Tool Integration**
   - Deep linking between tools
   - JIRA ↔ GitLab ↔ Jenkins integration
   - Automated status updates

4. **Mobile Access**
   - Mobile-friendly interfaces
   - Push notifications for build status

5. **Self-Service**
   - Developers can create their own projects/repos
   - Automated provisioning
   - Less waiting for admin approval

6. **Better Documentation**
   - Clear guides in Confluence
   - Video tutorials
   - Onboarding documentation

### Upgrade and Maintenance Improvements

**Current Gaps:**
- Manual server configuration → **Infrastructure as Code**
- Difficult updates → **Automated updates/blue-green deployment**
- Downtime for upgrades → **High availability setup**
- No backup automation → **Automated backups**

**Specific Improvements:**
1. **Infrastructure as Code (IaC)**
   - Terraform, Ansible, CloudFormation
   - Version-controlled infrastructure
   - Repeatable deployments
   - Easy disaster recovery

2. **Containerization**
   - Docker containers for all tools
   - Kubernetes for orchestration
   - Easy updates (replace container)
   - Consistent environments

3. **Automated Backups**
   - Scheduled automated backups
   - Regular restore testing
   - Off-site backup storage

4. **Blue-Green Deployment**
   - Two identical environments
   - Switch between them for updates
   - Zero downtime
   - Easy rollback

5. **Configuration Management**
   - Ansible, Puppet, Chef
   - Automated configuration
   - Drift detection

6. **Monitoring and Alerting**
   - Prometheus, Grafana
   - Proactive issue detection
   - Performance monitoring

### CI/CD Infrastructure Improvements

**Current Gaps:**
- Manual deployments → **Fully automated pipeline**
- No staging environment → **Add staging/pre-prod**
- Slow builds → **Parallel execution, caching**
- No deployment visibility → **Deployment dashboards**

**Specific Improvements:**
1. **Staging/Pre-Production Environment**
   - Test deployments before production
   - Production-like environment
   - Automated promotion from staging to prod

2. **Automated Deployment Pipeline**
   - Build → Test → Deploy automatically
   - Feature flags for gradual rollout
   - Automated rollback on failure

3. **Pipeline Optimization**
   - Parallel test execution
   - Build caching
   - Incremental builds
   - Faster feedback

4. **Agent Scalability**
   - Auto-scaling Jenkins agents
   - Cloud-based agents for burst capacity
   - Container-based agents

5. **Deployment Strategies**
   - Blue-green deployment
   - Canary releases
   - Rolling updates

6. **Observability**
   - Deployment tracking
   - Build metrics
   - Pipeline performance analytics

### Improvements from Other Courses

**From Security Course:**
- Vulnerability scanning
- Penetration testing
- Security headers
- Input validation
- Encryption at rest and in transit

**From Provisioning/Infrastructure Course:**
- Infrastructure as Code (Terraform, CloudFormation)
- Configuration management (Ansible)
- Immutable infrastructure
- Automated provisioning

**From Containerization Course:**
- Docker for all services
- Kubernetes orchestration
- Container registries
- Microservices architecture
- Service mesh (Istio)

**From Microservices Course:**
- API gateway
- Service discovery
- Circuit breakers
- Distributed tracing

---

## Key Review Topics

### Production Environment Management

**What is Production?**
- The **live environment** where end users access the software
- Mission-critical
- Requires careful management

**Before Updating Production:**
1. **Create rollback plan** ✓
2. **Test in staging** ✓
3. **Backup current state** ✓
4. **Notify stakeholders** ✓
5. **NOT**: Skip notifications, try to fix on the fly

**When to Update Production:**
- **During low-traffic periods** outside business hours
- NOT during peak hours
- NOT randomly
- Scheduled maintenance windows

**If Something Goes Wrong:**
- **Execute rollback plan immediately**
- Don't try to fix in production
- Don't wait to see if it fixes itself

**Rollback Plan:**
- Created **BEFORE** the update (not after)
- Tested and documented
- Quick to execute

### Enterprise Systems Review

**What is an Enterprise System?**
- Large-scale organization systems
- Organization-wide usage
- Multiple users and stakeholders
- Complex integration requirements

**Enterprise System Integration:**
- Connecting systems to work together
- Improves efficiency
- Reduces manual work
- Enables automation

**Relationship to EDE:**
- EDE is an example of enterprise system integration
- Integrates development tools
- Creates cohesive development ecosystem

**Why Have It?**
- Efficiency
- Quality
- Collaboration
- Standardization
- Faster delivery

### Static Code Analysis Review

**What is it?**
- **Inspection of code without execution**
- Automated analysis of source code
- Finds issues before runtime

**Benefits:**
1. Ensures compliance with coding standards
2. Finds dormant errors
3. Reduces manual review effort

**Static + Dynamic Analysis:**
- Together called **Glass Box Testing**

**SonarQube Quality Gates:**
- Set of conditions for release readiness
- Can enforce immediately (don't wait for all code to meet standard)
- New code meets standard, old code improved over time

### Components and Architecture

**Jenkins Components:**
1. **Controller**: Web server, brains
2. **Agent**: Runs stages
3. **Executor**: Manages tasks on node
4. **Node**: Same as agent

**SonarQube Components:**
1. **Server**: Web interface, compute
2. **Scanners**: Analyze code
3. **Plugins**: Language support
4. **Database**: Store data

**Where to Start SonarQube Analysis:**
- **SonarLint in the IDE** (best practice)
- Catch issues before commit

### Requirements Classification

**Functional Requirement Examples:**
- "System bills credit card after order"
- "System generates monthly report"
- "System sends email notification"

**Non-Functional Requirement Examples:**
- "System works on Chrome, Firefox, Safari" (Compatibility)
- "System handles 2M concurrent users" (Scalability)
- "Must restore within 8 hours" (Availability)

### Database and Installation

**Supported Databases (JIRA/Confluence Production):**
- Oracle
- PostgreSQL
- MySQL
- Microsoft SQL Server
- NOT: Embedded H2 (development only)

**Installation Methods:**
- Multiple methods available
- OS-specific installers (Windows, Linux)
- Archive files
- Docker containers

### Artifact Repository

**Advantages over File System:**
- **Artifacts are versioned** ✓
- Centralized management
- Controlled access
- Better than: plain files, just compression, just tags

**Key Characteristics:**
- Artifacts are version controlled ✓
- Artifacts are shared ✓

---

## Quick Reference - Key Facts

### True/False Quick Hits
- ✓ EDE can be on-premise, cloud, or both
- ✓ Infrastructure Automation = code in SCM
- ✗ Continuous Delivery ≠ manual daily deploys (it's automated)
- ✓ Pipeline is model of CI/CD process
- ✓ Stage = distinct subset of tasks
- ✗ Best practice ≠ pipeline in Jenkins job (should be in SCM)
- ✓ Agent and Node are effectively the same
- ✓ DevOps = ops and dev together through lifecycle
- ✗ Build break ≠ everyone drops everything (but it's high priority)
- ✓ Stakeholder = anyone with interest in system
- ✓ Shared libraries = reduce redundancy
- ✗ Quality gates ≠ wait for all code (can enforce immediately)
- ✓ SonarQube snapshot = measures at point in time
- ✗ NFRs ≠ define what system does (that's functional)
- ✓ Database schemas go in source control
- ✗ Rollback plan ≠ created after update
- ✗ Global libraries ≠ only specific jobs (available to all)

### Multiple Choice Quick Hits
- Integrate enterprise systems? **Improve efficiency**
- JIRA capability? **Work Management**
- Jenkins file name? **Jenkinsfile**
- Jenkins brains? **Controller**
- Manages execution on node? **Executor**
- Runs stages? **Agent**
- DevOps practice areas? **CD, IaC, SRE**
- CI server? **Build runs on every code change**
- Trigger pipeline? **Change to source code**
- Shared library language? **Groovy**
- Static analysis? **Inspection without execution**
- SonarQube scanner? **Client app that analyzes code**
- Enterprise? **Company with multiple employees**
- IaaS vs SaaS? **Infrastructure vs Complete applications**
- SaaS example? **Salesforce**
- Best time for prod update? **Low-traffic outside business hours**
- If prod update fails? **Execute rollback immediately**

---

## Study Tips

1. **Understand concepts, not just memorize**
   - Why do we use these tools?
   - How do they work together?
   - What problems do they solve?

2. **Know stakeholder perspectives**
   - What does each role care about?
   - How do their concerns differ?

3. **Practice scenario-based thinking**
   - Given a situation, what would you recommend?
   - Why one approach over another?

4. **Review tool capabilities**
   - What does each tool do?
   - How do they integrate?

5. **Understand workflows**
   - Different branching strategies
   - CI/CD pipeline flow
   - DevOps practices

6. **Know the architecture**
   - How components communicate
   - Authentication and authorization
   - Infrastructure patterns

Good luck on your final exam! 🎓