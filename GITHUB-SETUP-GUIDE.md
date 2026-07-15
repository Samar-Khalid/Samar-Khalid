# GitHub Profile Optimization Guide

> Complete guide to setting up your GitHub profile for maximum impact

---

## 1. PINNED REPOSITORIES

### Recommended Pin Order

| Position | Repository | Why |
|----------|-----------|-----|
| 1 | Prism-Analytics | Your flagship project |
| 2 | Prism-Enterprise-Benchmark | Shows AI + Enterprise focus |
| 3 | Codex-Enterprise | Enterprise application skills |
| 4 | Prism-Data-Generator | Data engineering skills |
| 5 | Odoo-Custom-Modules | ERP expertise |
| 6 | AI-BI-Learning | Learning mindset |

### How to Pin

1. Go to your GitHub profile
2. Click "Customize your pins"
3. Select the 6 repositories above
4. Click "Update pins"

---

## 2. REPOSITORY TOPICS & DESCRIPTIONS

### Prism-Analytics

**Description:**
```
AI-powered manufacturing analytics platform with NL2SQL, anomaly detection, and intelligent reporting
```

**Topics:**
```
ai
machine-learning
manufacturing
analytics
nl2sql
business-intelligence
python
fastapi
postgresql
enterprise
```

---

### Prism-Enterprise-Benchmark

**Description:**
```
100% synthetic benchmark dataset for evaluating AI models on enterprise manufacturing scenarios
```

**Topics:**
```
benchmark
dataset
synthetic-data
enterprise
manufacturing
ai
machine-learning
nl2sql
evaluation
research
```

---

### Codex-Enterprise

**Description:**
```
Modular framework for building AI-powered enterprise applications
```

**Topics:**
```
enterprise
framework
ai
fastapi
react
postgresql
redis
docker
microservices
```

---

### Prism-Data-Generator

**Description:**
```
Generate realistic synthetic manufacturing data for testing and benchmarking
```

**Topics:**
```
data-generator
synthetic-data
manufacturing
testing
benchmark
python
faker
```

---

### Odoo-Custom-Modules

**Description:**
```
Custom Odoo ERP modules with AI integration for manufacturing operations
```

**Topics:**
```
odoo
erp
manufacturing
python
ai
enterprise
workflow-automation
```

---

### AI-BI-Learning

**Description:**
```
Structured learning path combining AI/ML with Business Intelligence for enterprise solutions
```

**Topics:**
```
learning
ai
business-intelligence
power-bi
python
sql
machine-learning
```

---

## 3. ABOUT SECTIONS (GitHub Profile)

### Headline
```
AI Engineer | Enterprise Systems | Business Intelligence
```

### Bio
```
Building AI-powered solutions for enterprise manufacturing. 
Transforming data into intelligent decisions.
```

### Location
```
Egypt (or your location)
```

### Website
```
your-portfolio-url.com
```

### Social Links
```
LinkedIn: your-linkedin-url
Twitter: your-twitter-url (optional)
```

---

## 4. SOCIAL PREVIEW IMAGES

### Design Guidelines

Each repo needs a social preview image (1280x640px).

**Style:**
- Dark background (#0D1117 or #161B22)
- Clean typography
- Project name prominent
- One-line description
- Tech stack icons

### Templates

#### Prism-Analytics
```
Background: #0D1117 (GitHub dark)
Title: "Prism Analytics"
Subtitle: "AI-Powered Manufacturing Analytics"
Icons: Python, OpenAI, PostgreSQL
Tagline: "From Data to Decisions"
```

#### Prism-Enterprise-Benchmark
```
Background: #0D1117
Title: "Enterprise Benchmark"
Subtitle: "100% Synthetic Manufacturing Data"
Icons: Python, CSV, SQL
Tagline: "Evaluate AI Models"
```

#### Codex-Enterprise
```
Background: #0D1117
Title: "Codex Enterprise"
Subtitle: "Enterprise Application Framework"
Icons: FastAPI, React, Docker
Tagline: "Build Enterprise Apps"
```

#### Prism-Data-Generator
```
Background: #0D1117
Title: "Data Generator"
Subtitle: "Synthetic Manufacturing Data"
Icons: Python, JSON, CSV
Tagline: "Generate Realistic Data"
```

#### Odoo-Custom-Modules
```
Background: #0D1117
Title: "Odoo Modules"
Subtitle: "Custom ERP Solutions"
Icons: Odoo, Python, PostgreSQL
Tagline: "Extend Your ERP"
```

#### AI-BI-Learning
```
Background: #0D1117
Title: "AI BI Learning"
Subtitle: "AI + Business Intelligence"
Icons: Python, Power BI, SQL
Tagline: "Learn & Build"
```

---

## 5. HOW TO SET TOPICS

### Method 1: GitHub Web UI

1. Go to repository
2. Click gear icon next to "About"
3. Add description
4. Add topics (one by one)
5. Click "Save changes"

### Method 2: GitHub CLI

```bash
# Install GitHub CLI
winget install GitHub.cli

# Login
gh auth login

# Set topics
gh repo edit username/Prism-Analytics --add-topic ai,machine-learning,manufacturing
```

### Method 3: API

```bash
curl -X PATCH \
  -H "Authorization: token YOUR_TOKEN" \
  -H "Accept: application/vnd.github.mercy-preview+json" \
  https://api.github.com/repos/USERNAME/REPO \
  -d '{"topics": ["ai", "machine-learning", "manufacturing"]}'
```

---

## 6. SOCIAL PREVIEW IMAGES

### Create with Canva (Free)

1. Go to canva.com
2. Create custom design: 1280x640px
3. Use dark background (#0D1117)
4. Add project name
5. Add subtitle
6. Add tech icons
7. Download as PNG
8. Upload to GitHub repo settings

### Create with Figma (Free)

1. Create new frame: 1280x640
2. Set dark background
3. Add text and icons
4. Export as PNG
5. Upload to GitHub

### Simple HTML Template

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      background: #0D1117;
      color: white;
      font-family: -apple-system, BlinkMacSystemFont, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .card {
      text-align: center;
      padding: 40px;
    }
    h1 {
      font-size: 48px;
      margin-bottom: 10px;
    }
    h2 {
      font-size: 24px;
      color: #8B949E;
      font-weight: normal;
    }
    .tech {
      margin-top: 30px;
      color: #58A6FF;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>Prism Analytics</h1>
    <h2>AI-Powered Manufacturing Analytics</h2>
    <div class="tech">Python • OpenAI • PostgreSQL</div>
  </div>
</body>
</html>
```

---

## 7. CHECKLIST

- [ ] Pin 6 repositories in correct order
- [ ] Set descriptions for all repos
- [ ] Add topics to all repos
- [ ] Create social preview images
- [ ] Upload preview images
- [ ] Update profile README
- [ ] Set profile headline
- [ ] Add bio
- [ ] Add location
- [ ] Add website
- [ ] Add social links

---

## 8. RESULTS

After completing all steps:

**When someone visits your profile, they see:**
1. "AI Engineer | Enterprise Systems | Business Intelligence"
2. Professional profile README
3. 6 pinned repos with clear purpose
4. Consistent branding across all repos
5. Clear focus on Enterprise AI

**First impression in 5 seconds:**
> "This person specializes in AI for enterprise manufacturing systems."
