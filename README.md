# 서울 지하철 물품보관함 사용 현황 분석 시스템(Storage Project)

서울교통공사 Open API와 자체 수집 데이터를 기반으로
역별 물품보관함 가동률을 분석하기 위한 데이터 수집·저장·분석 프로젝트

관련 블로그 : https://blog.naver.com/uee8351773/224090984156

## How to Run

1. Create PostgreSQL database
2. Apply schema.sql
3. Set .env file
4. Run inventory loader
5. Run usage fetch job

## 1️⃣ 프로젝트 개요

이 프로젝트는 서울 지하철 역사 내 물품보관함 데이터를 수집하여
역별·규모별(소형/중형/대형) 물품보관함 사용 현황과 가동률을 분석하기 위한 데이터 파이프라인 구축을 목표로 합니다.

실시간에 가까운 API 데이터 수집

PostgreSQL 기반 데이터 정합성 관리

실제 무인화 사업(물품보관함, 무인매장) 입지 판단을 위한 데이터 기반 분석

## 2️⃣ 프로젝트 목표

📊 역별 물품보관함 가동률 분석

🏢 사용률이 높은 역을 사업 후보지로 식별

🔄 5분 단위로 갱신되는 API 데이터를 지속적으로 적재

🧱 향후 시각화 / 대시보드 확장 가능 구조 설계

## 3️⃣ 사용 기술 스택
Backend / Data

Python 3.11

Pandas

Requests

SQLAlchemy

PostgreSQL

Data Source

서울교통공사 Open API

물품보관함 위치 및 사용 가능 현황 (getFcLckr)

Development Environment

VS Code

Jupyter Notebook

Git / GitHub

## 4️⃣ 시스템 아키텍처

서울교통공사 Open API
        ↓
Python API Client
        ↓
PostgreSQL (stations / locker_inventory / locker_usage)
        ↓
Jupyter Notebook 분석

## 5️⃣ 데이터베이스 설계

📍 stations

지하철 역 기본 정보 (고정 데이터)

📦 locker_inventory

역별 물품보관함 수량 정보

소형 / 중형 / 대형 보관함 개수

CSV 기반 정적 데이터

🔄 locker_usage

API를 통해 수집되는 실시간 사용 현황

5분 단위 또는 수시 갱신

역별·규모별 사용 중인 보관함 수 기록

모든 테이블은 station_id를 기준으로 Foreign Key 관계를 유지합니다.

## 6️⃣ 데이터 수집 방식
🔹 실시간 사용 데이터

서울교통공사 Open API 호출

동일한 역 데이터라도 관측 시점(observed_at) 기준으로 누적 저장

중복 방지를 위해 (station_id, observed_at) 기준 관리

🔹 보관함 수량 데이터

공식 문서 기반 CSV 파일 수집

stations 테이블과 병합 후 inventory 테이블 적재

## 7️⃣ 현재 구현 상태

✅ 모든 테이블 데이터 적재 완료

✅ API 호출 및 usage 데이터 자동 갱신 확인

✅ DB 무결성(FK) 유지

✅ Jupyter Notebook 기반 분석 환경 구성 완료

## 8️⃣ 분석 예시 (1차)

역별 전체 물품보관함 가동률

소형 / 중형 / 대형 보관함 사용률

최고 가동률 역 Top N 분석

분석 로직은 지속적으로 확장 예정

## 9️⃣ 이 프로젝트가 의미 있는 이유

단순 시각화가 아닌 실제 사업 의사결정에 사용 가능한 데이터 구조

API → DB → 분석까지 전 과정을 직접 설계 및 구현

무인화·스마트 인프라 사업과 직접 연결되는 현실적인 문제 해결