# 機能一覧

## 従業員一覧・詳細表示機能

- [ ] 従業員概要一覧表示
- [ ] 従業員情報詳細表示

## 従業員プロフィール管理・編集機能

- [ ] プロフィールの編集・更新
- [ ] 登録プロフィールのファイルへのエクスポート

## 出退勤登録機能

- [ ] 出勤登録
- [ ] 退勤登録

## 勤務状況閲覧機能

### 全員

- [ ] 月次
- [ ] 週次
- [ ] 日次

### 個人

- [ ] 年次
- [ ] 月次
- [ ] 週次

## 子供見守り機能

- [ ] 子供の来園登録（ワンタッチ自動登録）
- [ ] 子供の退園登録（ワンタッチ自動登録）

## 集金管理機能

- [ ] 集金カテゴリの一覧表示
- [ ] 集金カテゴリ新規登録
- [ ] 集金カテゴリの属性情報編集
- [ ] 集金対象者の抽出と集金ステータス表示
- [ ] 集金対象者の連絡先情報確認

# API 一覧

## Query

### 従業員取得

- [x] employee
- [x] employees

### 職級取得

- [x] jobs

### 園児取得

- [x] child
- [x] children

### 子供部屋情報取得

- [x] classroom
- [x] classrooms

### 集金情報取得

- [ ] finance
- [ ] finances

### 勤怠状況取得

- [ ] employees_daily
- [ ] employees_weekly
- [ ] employees_monthly
- [ ] employee_annually

### 登退園情報取得

- [ ] childs_daily
- [ ] childs_weekly
- [ ] childs_monthly

## Mutation

### 職級操作

- [x] job_create
- [ ] job_update
- [ ] job_delete

### 従業員データ操作

- [x] employee_create
- [ ] employee_update
- [ ] employee_delete

### 園児データ操作

- [x] child_create
- [ ] child_update
- [ ] child_delete

### 子供部屋データ操作

- [x] classroom_create
- [ ] classroom_update
- [ ] classroom_delete

### 出退勤登録

- [ ] employee_daily_insert

### 登退園登録

- [ ] child_daily_insert

### 集金カテゴリ操作

- [ ] finance_create
- [ ] finance_update
- [ ] finance_delete
- [ ] finance_confirm
