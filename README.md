# VulnForge

### Security Research & Analysis Platform

> A modular security research platform focused on structured findings, plugin-based analysis, and professional reporting.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Version](https://img.shields.io/badge/Version-0.1.0-green)
![Status](https://img.shields.io/badge/Status-v0.3.0-blue)

## Overview

VulnForge is a modular platform designed for authorized security research, analysis, testing, and reporting.

The project focuses on clean architecture rather than simply combining existing security tools.

## Architecture

```text
CLI
 │
 ▼
Configuration
 │
 ▼
Core Engine
 │
 ▼
Plugin Registry
 │
 ▼
Security Plugins
 │
 ▼
Findings
 │
 ├── JSON Report
 └── HTML Report

ls
