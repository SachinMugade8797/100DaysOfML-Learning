Checkout My Project 

Alerting-Notification-Platform Project Link - https://github.com/SachinMugade8797/Alerting-Notification-Platform




# Alerting-Notification-Platform
Project Assignment 



# 🔔 Alerting & Notification Platform

A comprehensive alerting system built with Flask that enables organizations to manage notifications efficiently with advanced user experience features and real-time status tracking.

## 📸 Screenshots

### Home Page

<img width="1920" height="1080" alt="Screenshot 2025-09-26 194427" src="https://github.com/user-attachments/assets/583c54f5-55a3-4fd9-8110-3c3b43934036" />




### Admin Dashboard
<img width="1920" height="1080" alt="Screenshot 2025-09-26 194519" src="https://github.com/user-attachments/assets/dc3509e4-f433-40f3-b659-c10b0603f8b3" />
*Admin interface showing active alerts with read status indicators and reminder controls*


### User Dashboard
## User 1 - Team: Engineering
<img width="1920" height="1080" alt="Screenshot 2025-09-26 194655" src="https://github.com/user-attachments/assets/92ad3697-070b-4ce8-8e86-ca22df6ccc34" />
*User interface displaying relevant alerts with action buttons if sunnuze button appear only if the Admin Enable reminders*

## User 2 - Team: Marketing
<img width="1920" height="1080" alt="Screenshot 2025-09-26 194709" src="https://github.com/user-attachments/assets/0c875b1a-bc04-400d-b86e-9acb43abc060" />


### Creating New Alert
<img width="1920" height="1080" alt="Screenshot 2025-09-26 201652" src="https://github.com/user-attachments/assets/e66eea47-e1db-4f5e-affc-5393c98074e4" />

*Alert creation form with visibility targeting and reminder settings*

<img width="1920" height="1080" alt="Screenshot 2025-09-26 201829" src="https://github.com/user-attachments/assets/419dada1-655e-4a39-a157-56184fa4bd9b" />


### Popup Notification
<img width="1920" height="1080" alt="Screenshot 2025-09-26 201851" src="https://github.com/user-attachments/assets/96a41031-ea76-4231-b229-4c3f7ab33b4d" />

*Real-time popup notification for new alerts*


<img width="1920" height="1080" alt="Screenshot 2025-09-26 201908" src="https://github.com/user-attachments/assets/69bd2db1-a85c-407b-a2de-0926fb12188c" />



### Read Status Tracking
<img width="1920" height="1080" alt="Screenshot 2025-09-26 201924" src="https://github.com/user-attachments/assets/7936b000-b8f2-490f-bec6-265b61a0099f" />

*WhatsApp-style read indicators showing alert engagement*

### Intelligent Snooze 

<img width="1920" height="1080" alt="Screenshot 2025-09-26 201941" src="https://github.com/user-attachments/assets/70ce5f7b-bed3-4ffa-9876-f08def6216d9" />


### Delete Confirmation
<img width="1920" height="1080" alt="Screenshot 2025-09-26 202036" src="https://github.com/user-attachments/assets/795050fc-aacc-4c2b-b0e8-fef9547e325b" />

*Admin alert deletion with confirmation dialog*

<img width="1920" height="1080" alt="Screenshot 2025-09-26 202050" src="https://github.com/user-attachments/assets/21b9e5f3-433d-4b1e-9f35-0f6d8745cc0f" />


## ✨ Features

### Admin Capabilities
- **📝 Create Unlimited Alerts** - Title, message, severity (Info/Warning/Critical)
- **🎯 Flexible Targeting** - Organization-wide, specific teams, or individual users
- **🔔 Reminder Management** - Enable/disable automatic reminders per alert
- **📊 Read Status Tracking** - WhatsApp-style indicators showing who read what
- **🗑️ Alert Management** - Delete outdated or incorrect alerts
- **📈 Real-time Analytics** - See read percentages and user engagement

### User Experience
- **🔔 Smart Notifications** - Popup alerts for new notifications
- **✅ Mark as Read** - Simple one-click acknowledgment
- **😴 Intelligent Snooze** - Snooze for the day (only shown when reminders enabled)
- **📱 Instant Feedback** - Toast notifications for all actions
- **🎨 Clean Interface** - Professional, responsive design

### Technical Excellence
- **🏗️ Modular Architecture** - Clean separation of concerns (MVC pattern)
- **🗄️ Proper Database Design** - Relational structure with foreign keys
- **🔒 Error Handling** - Comprehensive exception management
- **📡 RESTful APIs** - Clean JSON endpoints for frontend interactions
- **🚀 Extensible Code** - Easy to add new features and notification channels

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Database**: SQLAlchemy ORM with SQLite
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Architecture**: MVC Pattern
- **APIs**: RESTful JSON endpoints

## 📋 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Quick Start
```bash
# 1. Clone or download the project
git clone <your-repo-url>
cd alert-system

# 2. Install dependencies
pip install flask flask-sqlalchemy

# 3. Run the application
python app.py

# 4. Open your browser
http://localhost:5000
```

### Project Structure
```
alert-system/
├── app.py                 # Main Flask application
├── templates/            
│   ├── base.html         # Common layout and JavaScript
│   ├── home.html         # Landing page
│   ├── admin_dashboard.html   # Admin interface
│   ├── create_alert.html     # Alert creation form
│   └── user_dashboard.html   # User interface
├── instance/      # SQLite database
└── README.md

```

## 🎮 Demo & Usage

### Sample Users 
- **Admin User**: Full access to create and manage alerts
- **John Doe**: Engineering team member (User ID: 2)
- **Jane Smith**: Marketing team member (User ID: 3)

### Quick Demo Flow
1. **Start Here**: Visit `http://localhost:5000`
2. **Admin Demo**: Go to Admin Dashboard → Create Alert
3. **User Demo**: Visit John's or Jane's Dashboard
4. **Try Features**: Mark as read, snooze, delete alerts



## 🗃️ Database Schema

### Core Tables
- **User**: User information and team membership
- **Team**: Team organization structure
- **Alert**: Alert content and settings
- **UserAlertStatus**: Read/snooze status tracking per user

### Key Relationships
```sql
User.team_id → Team.id
Alert.created_by → User.id
Alert.target_team_id → Team.id (optional)
Alert.target_user_id → User.id (optional)
UserAlertStatus.user_id → User.id
UserAlertStatus.alert_id → Alert.id
```

## 🎯 Current Implementation Status

### ✅ Completed Features (MVP Ready)
- **Admin Alert Management** (100%)
  - Create alerts with all targeting options
  - Delete alerts with cleanup
  - Enable/disable reminders per alert
  - Real-time read status tracking

- **User Experience** (100%)
  - Dashboard with relevant alerts
  - Mark as read functionality
  - Smart snooze (only when reminders enabled)
  - Popup notifications for new alerts

- **Technical Foundation** (100%)
  - Clean MVC architecture
  - RESTful API endpoints
  - Error handling and validation
  - Professional UI/UX design

### 📊 Feature Completion: 75%

## 🚀 Future Enhancements

Based on the original requirements, here are planned improvements:

### Phase 1: Core Reminder System
- **⏰ Automatic 2-Hour Reminders**
  - Background task scheduler
  - Email/SMS integration
  - Escalation logic for unread alerts

### Phase 2: Advanced Analytics
- **📈 Analytics Dashboard**
  - System-wide metrics
  - Alerts delivered vs. read ratios
  - User engagement patterns
  - Severity breakdown charts

### Phase 3: Enterprise Features
- **🔐 Role-Based Access Control**
  - Multiple admin levels
  - Department-based permissions
  - User management interface

- **📅 Advanced Scheduling**
  - Customizable reminder frequencies
  - Scheduled alerts (cron-like)
  - Time zone support

- **📧 Multi-Channel Delivery**
  - Email notifications
  - SMS integration
  - Push notifications
  - Slack/Teams integration

### Phase 4: Scalability & Performance
- **🔄 Real-time Updates**
  - WebSocket integration for live updates
  - Real-time read status changes
  - Live notification delivery

- **📱 Mobile Optimization**
  - Progressive Web App (PWA)
  - Mobile-first responsive design
  - Offline capability

## 🏗️ Architecture Decisions

### Why Flask?
- **Lightweight**: Perfect for MVPs and rapid prototyping
- **Flexible**: Easy to extend and customize
- **Simple**: Minimal learning curve for beginners

### Why SQLAlchemy?
- **ORM Benefits**: Object-oriented database interactions
- **Database Agnostic**: Easy to switch from SQLite to PostgreSQL
- **Relationship Management**: Proper foreign key handling

### Design Patterns Used
- **MVC Architecture**: Clean separation of concerns
- **RESTful APIs**: Consistent endpoint design
- **Progressive Enhancement**: Works with basic HTML, enhanced with JavaScript



