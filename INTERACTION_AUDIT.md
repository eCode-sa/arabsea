# Interaction Audit

Page-by-page inventory of controls across **114 HTML pages**. Button categories use the same static action map as `scripts/qa_audit.py`. A-J categories are code-path classifications and have not been browser-verified; K actions explicitly explain that no backend operation ran.

## Button totals

- Total buttons: **1128**
- A. Navigation: **16**
- A. Navigation / pagination: **93**
- A. Navigation / shared shell: **330**
- B. Modal / drawer: **3**
- C. Create (business schema): **45**
- D. Edit: **41**
- E. Workflow action: **94**
- F. Filter: **20**
- G. Export: **62**
- H. Download / preview: **190**
- I. Communication: **13**
- J. Settings: **25**
- K. Backend-dependent (explicit explanation; no fake completion): **196**
- Generic Page Action / generic Create Record fallbacks: **0**
- Business form schemas in `assets/js/core/actions.js`: **33**

## Page summary

| Page | Buttons | Links | Fields |
|---|---:|---:|---:|
| `admin/admin_chat.html` | 10 | 20 | 2 |
| `admin/admin_circulars.html` | 9 | 20 | 0 |
| `admin/admin_settings.html` | 12 | 20 | 7 |
| `admin/audit.html` | 9 | 20 | 0 |
| `admin/board.html` | 6 | 28 | 0 |
| `admin/committees.html` | 4 | 24 | 0 |
| `admin/compliance.html` | 5 | 20 | 0 |
| `admin/doa.html` | 4 | 20 | 2 |
| `admin/finance.html` | 11 | 23 | 0 |
| `admin/ga.html` | 6 | 20 | 0 |
| `admin/hr.html` | 10 | 20 | 0 |
| `admin/index.html` | 3 | 21 | 0 |
| `admin/it.html` | 7 | 20 | 0 |
| `admin/policies.html` | 16 | 20 | 1 |
| `admin/procurement.html` | 6 | 20 | 0 |
| `admin/profile.html` | 7 | 20 | 0 |
| `admin/shareholders.html` | 4 | 20 | 0 |
| `admin/tasks.html` | 5 | 20 | 1 |
| `admin/users.html` | 20 | 20 | 1 |
| `audit/audit_plan.html` | 16 | 9 | 4 |
| `audit/audit_reports.html` | 15 | 9 | 3 |
| `audit/index.html` | 3 | 12 | 0 |
| `audit/observations.html` | 17 | 9 | 3 |
| `audit/profile.html` | 3 | 9 | 0 |
| `audit/risk_reports.html` | 17 | 9 | 3 |
| `audit/working_papers.html` | 15 | 9 | 3 |
| `board/communication.html` | 5 | 11 | 2 |
| `board/finance.html` | 7 | 9 | 0 |
| `board/governance.html` | 8 | 9 | 0 |
| `board/index.html` | 6 | 11 | 0 |
| `board/meetings.html` | 13 | 9 | 1 |
| `board/profile.html` | 3 | 9 | 0 |
| `ceo/ceo_broadcast.html` | 5 | 12 | 4 |
| `ceo/ceo_communication.html` | 5 | 14 | 0 |
| `ceo/ceo_feedback.html` | 6 | 12 | 0 |
| `ceo/ceo_finance.html` | 3 | 12 | 0 |
| `ceo/ceo_governance.html` | 5 | 13 | 0 |
| `ceo/ceo_reports.html` | 7 | 12 | 0 |
| `ceo/ceo_risks.html` | 3 | 12 | 0 |
| `ceo/ceo_strategy.html` | 3 | 12 | 0 |
| `ceo/index.html` | 9 | 16 | 0 |
| `ceo/profile.html` | 2 | 12 | 0 |
| `cto/cto_assets.html` | 14 | 14 | 3 |
| `cto/cto_call_logs.html` | 13 | 14 | 3 |
| `cto/cto_extensions.html` | 14 | 14 | 3 |
| `cto/cto_iam.html` | 15 | 14 | 3 |
| `cto/cto_monitoring.html` | 7 | 14 | 0 |
| `cto/cto_pbx.html` | 10 | 14 | 2 |
| `cto/cto_projects.html` | 8 | 14 | 3 |
| `cto/cto_servers.html` | 17 | 14 | 3 |
| `cto/cto_soc.html` | 14 | 14 | 3 |
| `cto/cto_support.html` | 12 | 14 | 4 |
| `cto/index.html` | 3 | 16 | 0 |
| `cto/profile.html` | 3 | 14 | 0 |
| `employee/approvals.html` | 17 | 11 | 2 |
| `employee/cloud.html` | 20 | 12 | 5 |
| `employee/finance.html` | 15 | 11 | 3 |
| `employee/index.html` | 4 | 19 | 0 |
| `employee/performance.html` | 10 | 11 | 0 |
| `employee/policies.html` | 16 | 11 | 2 |
| `employee/profile.html` | 6 | 11 | 0 |
| `employee/requests.html` | 16 | 11 | 3 |
| `employee/support.html` | 14 | 11 | 3 |
| `finance/ap_bills.html` | 8 | 20 | 3 |
| `finance/ap_payments.html` | 12 | 20 | 3 |
| `finance/ap_vendors.html` | 17 | 20 | 2 |
| `finance/approvals.html` | 20 | 20 | 0 |
| `finance/ar_invoices.html` | 17 | 20 | 3 |
| `finance/ar_receipts.html` | 12 | 20 | 3 |
| `finance/fin_settings.html` | 6 | 20 | 13 |
| `finance/gl_coa.html` | 18 | 20 | 2 |
| `finance/gl_cost_centers.html` | 10 | 20 | 2 |
| `finance/gl_journal.html` | 14 | 20 | 3 |
| `finance/index.html` | 6 | 25 | 0 |
| `finance/internal_chat.html` | 7 | 20 | 2 |
| `finance/inv_assets.html` | 16 | 20 | 3 |
| `finance/inv_dashboard.html` | 5 | 20 | 2 |
| `finance/profile.html` | 2 | 20 | 0 |
| `finance/rep_budget.html` | 8 | 20 | 3 |
| `finance/rep_statements.html` | 11 | 20 | 4 |
| `finance/rep_tax.html` | 10 | 20 | 2 |
| `hr/hr_approvals.html` | 19 | 19 | 0 |
| `hr/hr_assets.html` | 17 | 19 | 3 |
| `hr/hr_attendance.html` | 14 | 19 | 4 |
| `hr/hr_contracts.html` | 17 | 19 | 3 |
| `hr/hr_employees.html` | 17 | 19 | 3 |
| `hr/hr_govt.html` | 13 | 19 | 3 |
| `hr/hr_leaves.html` | 16 | 19 | 3 |
| `hr/hr_logistics.html` | 16 | 19 | 3 |
| `hr/hr_org.html` | 7 | 19 | 0 |
| `hr/hr_partners.html` | 14 | 19 | 3 |
| `hr/hr_payroll.html` | 11 | 19 | 2 |
| `hr/hr_purchases.html` | 16 | 19 | 3 |
| `hr/hr_recruitment.html` | 17 | 19 | 3 |
| `hr/hr_trips.html` | 14 | 19 | 3 |
| `hr/index.html` | 6 | 24 | 0 |
| `hr/internal_chat.html` | 13 | 19 | 2 |
| `hr/profile.html` | 3 | 19 | 0 |
| `index.html` | 1 | 8 | 0 |
| `login.html` | 13 | 1 | 2 |
| `sales/index.html` | 3 | 13 | 0 |
| `sales/profile.html` | 3 | 10 | 0 |
| `sales/sales_activities.html` | 18 | 10 | 4 |
| `sales/sales_clients.html` | 17 | 10 | 3 |
| `sales/sales_contracts.html` | 13 | 10 | 3 |
| `sales/sales_pipeline.html` | 5 | 10 | 3 |
| `sales/sales_quotes.html` | 16 | 10 | 3 |
| `sales/sales_targets.html` | 9 | 10 | 3 |
| `shareholder/certificates.html` | 4 | 8 | 0 |
| `shareholder/dividends.html` | 4 | 8 | 0 |
| `shareholder/index.html` | 3 | 13 | 0 |
| `shareholder/profile.html` | 4 | 8 | 5 |
| `shareholder/requests.html` | 4 | 8 | 4 |
| `shareholder/voting.html` | 4 | 8 | 9 |

## Backend-dependent action list

These controls open an explanatory UI, preserve any useful record context, and state that the requested service action did not run.

- `admin/admin_chat.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `admin/admin_chat.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `admin/admin_chat.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `admin/admin_settings.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `admin/admin_settings.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `admin/board.html` — “[icon]” — K. Placeholder link; backend or route configuration required.
- `admin/board.html` — “[icon]” — K. Placeholder link; backend or route configuration required.
- `admin/board.html` — “[icon]” — K. Placeholder link; backend or route configuration required.
- `admin/board.html` — “[icon]” — K. Placeholder link; backend or route configuration required.
- `admin/board.html` — “[icon]” — K. Placeholder link; backend or route configuration required.
- `admin/board.html` — “[icon]” — K. Placeholder link; backend or route configuration required.
- `admin/board.html` — “[icon]” — K. Placeholder link; backend or route configuration required.
- `admin/board.html` — “[icon]” — K. Placeholder link; backend or route configuration required.
- `admin/committees.html` — “عرض محاضر الاجتماعات” — K. Placeholder link; backend or route configuration required.
- `admin/committees.html` — “[icon]” — K. Placeholder link; backend or route configuration required.
- `admin/committees.html` — “عرض محاضر الاجتماعات” — K. Placeholder link; backend or route configuration required.
- `admin/committees.html` — “[icon]” — K. Placeholder link; backend or route configuration required.
- `admin/finance.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `admin/finance.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `admin/finance.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `admin/finance.html` — “قائمة المركز المالي محدث: نهاية الربع الثالث” — K. Placeholder link; backend or route configuration required.
- `admin/finance.html` — “قائمة الدخل محدث: نهاية الربع الثالث” — K. Placeholder link; backend or route configuration required.
- `admin/finance.html` — “التدفقات النقدية يومي (متابعة السيولة)” — K. Placeholder link; backend or route configuration required.
- `admin/it.html` — “فرض التحديث الآن” — K. Backend-dependent (explicit explanation; no fake completion).
- `admin/users.html` — “مستخدم جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- `admin/users.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `admin/users.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `audit/audit_plan.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `audit/audit_plan.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `audit/audit_reports.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `audit/audit_reports.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `audit/observations.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `audit/observations.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `audit/risk_reports.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `audit/risk_reports.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `audit/working_papers.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `audit/working_papers.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `board/communication.html` — “تحميل المرفق (PDF)” — K. Placeholder link; backend or route configuration required.
- `board/communication.html` — “تحميل القرار” — K. Placeholder link; backend or route configuration required.
- `board/index.html` — “الاطلاع على حقيبة الاجتماع” — K. Backend-dependent (explicit explanation; no fake completion).
- `board/meetings.html` — “التقويم السنوي” — K. Backend-dependent (explicit explanation; no fake completion).
- `board/meetings.html` — “إضافة ملاحظة” — K. Backend-dependent (explicit explanation; no fake completion).
- `board/meetings.html` — “حقيبة الاجتماع” — K. Backend-dependent (explicit explanation; no fake completion).
- `ceo/ceo_communication.html` — “حقيبة الاجتماع” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_assets.html` — “تسليم لموظف” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_assets.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_assets.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_call_logs.html` — “استماع للتسجيل” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_call_logs.html` — “إرسال تنبيه بالبريد” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_call_logs.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_call_logs.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_extensions.html` — “إدارة المجموعة” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_extensions.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_extensions.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_iam.html` — “إرسال رابط التفعيل” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_iam.html` — “حذف نهائي” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_iam.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_iam.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_monitoring.html` — “إضافة نقطة مراقبة” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_pbx.html` — “إضافة خط جديد (Trunk)” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_projects.html` — “مخطط جانت (Gantt)” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_servers.html` — “إضافة خادم جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_servers.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_servers.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_soc.html` — “فحص شامل (Vulnerability Scan)” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_soc.html` — “عزل (Isolate)” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_soc.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_soc.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_support.html` — “تقرير الأداء” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_support.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `cto/cto_support.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/approvals.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/approvals.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/cloud.html` — “رفع ملفات جديدة” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/cloud.html` — “ملفاتي” — K. Placeholder link; backend or route configuration required.
- `employee/cloud.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/cloud.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/cloud.html` — “حذف” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/cloud.html` — “حذف” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/cloud.html` — “حذف” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/cloud.html` — “حذف” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/cloud.html` — “تصفح جهازك” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/finance.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/finance.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/index.html` — “تسجيل دخول (Punch In)” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/index.html` — “Policy_v2.pdf” — K. Placeholder link; backend or route configuration required.
- `employee/performance.html` — “صياغة هدف جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/performance.html` — “منصة التعليم” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/performance.html` — “متابعة” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/performance.html` — “البدء” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/profile.html` — “طلب تغيير” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/requests.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/requests.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/support.html` — “إضافة تعليق” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/support.html` — “إضافة تعليق” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/support.html` — “تقييم” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/support.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `employee/support.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/ap_bills.html` — “إضافة فاتورة مورد” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/ap_bills.html` — “تسجيل دفعة” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/ap_bills.html` — “تسجيل دفعة” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/ap_payments.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/ap_payments.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/ap_vendors.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/ap_vendors.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/ar_invoices.html` — “تسجيل دفعة” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/ar_invoices.html` — “تسجيل دفعة” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/ar_invoices.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/ar_invoices.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/ar_receipts.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/ar_receipts.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/gl_coa.html` — “إضافة حساب فرعي جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/gl_coa.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/gl_coa.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/gl_coa.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/gl_coa.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/gl_coa.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/gl_coa.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/gl_coa.html` — “كشف حساب” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/gl_coa.html` — “كشف حساب” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/gl_coa.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/gl_coa.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/gl_coa.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/gl_coa.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/gl_journal.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/gl_journal.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/internal_chat.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/internal_chat.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/internal_chat.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/internal_chat.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/inv_assets.html` — “تشغيل الإهلاك الشهري” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/inv_assets.html` — “سجل الإهلاك” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/inv_assets.html` — “سجل الإهلاك” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/inv_assets.html` — “سجل الإهلاك” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/inv_assets.html` — “استبعاد / بيع” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/inv_assets.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/inv_assets.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/rep_budget.html` — “تخصيص موازنة جديدة” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/rep_budget.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/rep_budget.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/rep_budget.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/rep_statements.html` — “المركز المالي (الميزانية)” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/rep_statements.html` — “التدفقات النقدية” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/rep_statements.html` — “تحديث التقرير” — K. Backend-dependent (explicit explanation; no fake completion).
- `finance/rep_tax.html` — “الشهادة الزكوية” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_assets.html` — “تسليم عهدة جديدة” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_assets.html` — “إصدار بدل فاقد” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_assets.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_assets.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_attendance.html` — “سحب حركات البصمة” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_attendance.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_attendance.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_contracts.html` — “تجديد العقد” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_contracts.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_contracts.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_employees.html` — “الملف الشخصي” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_employees.html` — “الملف الشخصي” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_employees.html` — “الملف الشخصي” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_employees.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_employees.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_govt.html` — “مزامنة البيانات” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_govt.html` — “الدخول للمنصات” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_govt.html` — “إرسال طلب للمالية” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_govt.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_govt.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_leaves.html` — “المرفق (التقرير الطبي)” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_leaves.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_leaves.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_logistics.html` — “طلب خدمة جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_logistics.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_logistics.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_partners.html` — “بوابة الشريك (الشبكة الطبية)” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_partners.html` — “تجديد العقد” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_partners.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_partners.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_payroll.html` — “إنشاء مسير الشهر الحالي” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_payroll.html` — “إرسال للمالية” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_purchases.html` — “متابعة مع المشتريات” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_purchases.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_purchases.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_recruitment.html` — “لوحة الوظائف” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_recruitment.html` — “إدارة المقابلة” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_recruitment.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_recruitment.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_trips.html` — “تسجيل انتداب جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_trips.html` — “التذاكر والمرفقات” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_trips.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/hr_trips.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/index.html` — “بدء إجراءات التجديد” — K. Placeholder link; backend or route configuration required.
- `hr/index.html` — “طلب تقييم المدراء” — K. Placeholder link; backend or route configuration required.
- `hr/internal_chat.html` — “الإدارات” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/internal_chat.html` — “الاستفسارات” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/internal_chat.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/internal_chat.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `hr/internal_chat.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `login.html` — “نسيت كلمة المرور؟” — K. Placeholder link; backend or route configuration required.
- `login.html` — “دخول النظام” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_activities.html` — “مزامنة مع Outlook” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_activities.html` — “إعادة جدولة” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_activities.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_activities.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_clients.html` — “ملف العميل” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_clients.html` — “ملف العميل” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_clients.html` — “ملف العميل” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_clients.html` — “ملف العميل” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_clients.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_clients.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_contracts.html` — “تسجيل عقد جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_contracts.html` — “بدء تجديد العقد” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_contracts.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_contracts.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_pipeline.html` — “إضافة فرصة جديدة” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_quotes.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_quotes.html` — “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_targets.html` — “احتساب عمولات Q4” — K. Backend-dependent (explicit explanation; no fake completion).
- `sales/sales_targets.html` — “ضبط مستهدف جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- `shareholder/profile.html` — “تحديث كلمة المرور” — K. Backend-dependent (explicit explanation; no fake completion).
- `shareholder/requests.html` — “[icon]” — K. File picker only; secure upload storage requires backend.
- `shareholder/requests.html` — “إرسال الطلب” — K. Backend-dependent (explicit explanation; no fake completion).

## Control inventory

### `admin/admin_chat.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **input** “بحث في المحادثات...” — F. Current-page search/filter.
- **button** “مكالمة صوتية” — I. Communication.
- **button** “مكالمة مرئية” — I. Communication.
- **button** “معلومات المجموعة” — B. Modal / drawer.
- **button** “[icon]” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **textarea** “اكتب رسالة...” — Form field; page-specific form submission or backend integration.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `admin/admin_circulars.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “إصدار تعميم جديد” — C. Create (business schema).
- **button** “الكل” — F. Filter.
- **button** “قرارات إدارية” — F. Filter.
- **button** “الموارد البشرية” — F. Filter.
- **button** “تقنية المعلومات” — F. Filter.
- **button** “تأكيد القراءة” — E. Workflow action.

### `admin/admin_settings.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “بيانات الشركة” — J. Settings.
- **button** “الأمان وحماية البيانات” — J. Settings.
- **button** “التنبيهات والإشعارات” — A. Navigation / shared shell.
- **button** “الربط التقني (Integration)” — J. Settings.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **button** “تغيير الشعار” — J. Settings.
- **button** “حفظ التعديلات” — J. Settings.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “ربط” — J. Settings.

### `admin/audit.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “تقرير مراجعة جديد” — H. Download / preview.
- **button** “سجل المهام” — A. Navigation.
- **button** “[icon]” — H. Download / preview.
- **button** “[icon]” — H. Download / preview.
- **button** “[icon]” — H. Download / preview.
- **button** “إرسال تذكير للإدارة المعنية” — E. Workflow action.

### `admin/board.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “تحميل المحضر” — H. Download / preview.
- **button** “دعوة لاجتماع” — C. Create (business schema).
- **a** “[icon]” — K. Placeholder link; backend or route configuration required.
- **a** “[icon]” — K. Placeholder link; backend or route configuration required.
- **a** “[icon]” — K. Placeholder link; backend or route configuration required.
- **a** “[icon]” — K. Placeholder link; backend or route configuration required.
- **a** “[icon]” — K. Placeholder link; backend or route configuration required.
- **a** “[icon]” — K. Placeholder link; backend or route configuration required.
- **a** “[icon]” — K. Placeholder link; backend or route configuration required.
- **a** “[icon]” — K. Placeholder link; backend or route configuration required.
- **button** “مراسلة” — I. Communication.

### `admin/committees.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “إضافة لجنة جديدة” — C. Create (business schema).
- **a** “عرض محاضر الاجتماعات” — K. Placeholder link; backend or route configuration required.
- **a** “[icon]” — K. Placeholder link; backend or route configuration required.
- **a** “عرض محاضر الاجتماعات” — K. Placeholder link; backend or route configuration required.
- **a** “[icon]” — K. Placeholder link; backend or route configuration required.

### `admin/compliance.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “تسجيل خطر جديد” — C. Create (business schema).
- **button** “السجل الشامل” — A. Navigation.

### `admin/doa.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **input** “ابحث عن صلاحية...” — F. Current-page search/filter.
- **button** “تصدير (PDF)” — G. Export.
- **select** “جميع التصنيفات صلاحيات بنكية ومالية صلاحيات إدارية صلاحيات قانونية وتمثيل” — F. Native selection / table filter.

### `admin/finance.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “إنشاء أمر صرف” — H. Download / preview.
- **button** “السجل الكامل” — A. Navigation.
- **button** “[icon]” — E. Workflow action.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — E. Workflow action.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — E. Workflow action.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **a** “قائمة المركز المالي محدث: نهاية الربع الثالث” — K. Placeholder link; backend or route configuration required.
- **a** “قائمة الدخل محدث: نهاية الربع الثالث” — K. Placeholder link; backend or route configuration required.
- **a** “التدفقات النقدية يومي (متابعة السيولة)” — K. Placeholder link; backend or route configuration required.

### `admin/ga.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “إنشاء جمعية جديدة” — C. Create (business schema).
- **button** “محضر اجتماع الجمعية.pdf” — G. Export.
- **button** “تقرير إيداع (مستندات التصويت).pdf” — G. Export.

### `admin/hr.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “تصدير المسير” — G. Export.
- **button** “إضافة موظف” — C. Create (business schema).
- **button** “عرض الكل” — H. Download / preview.
- **button** “موافقة” — E. Workflow action.
- **button** “رفض” — E. Workflow action.
- **button** “موافقة” — E. Workflow action.
- **button** “رفض” — E. Workflow action.

### `admin/index.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **a** “عرض الكل” — A. Native navigation.

### `admin/it.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “تذكرة دعم فني” — C. Create (business schema).
- **button** “لوحة المشاريع” — A. Navigation.
- **button** “فرض التحديث الآن” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “مراجعة الطلبات” — E. Workflow action.

### `admin/policies.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **input** “ابحث في اللوائح...” — F. Current-page search/filter.
- **button** “تصفية” — F. Filter.
- **button** “استعراض” — H. Download / preview.
- **button** “استعراض” — H. Download / preview.
- **button** “استعراض” — H. Download / preview.
- **button** “استعراض” — H. Download / preview.
- **button** “استعراض” — H. Download / preview.
- **button** “عرض” — H. Download / preview.
- **button** “عرض” — H. Download / preview.
- **button** “عرض” — H. Download / preview.
- **button** “عرض” — H. Download / preview.
- **button** “عرض” — H. Download / preview.
- **button** “عرض” — H. Download / preview.
- **button** “عرض” — H. Download / preview.

### `admin/procurement.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “أمر شراء جديد (PO)” — C. Create (business schema).
- **button** “عرض جميع الطلبات” — H. Download / preview.
- **button** “إضافة مورد جديد للقائمة المعتمدة” — C. Create (business schema).

### `admin/profile.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “م. أيمن المغربي مدير النظام” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “تعديل البيانات” — D. Edit.
- **button** “السجل الكامل” — A. Navigation.
- **button** “تغيير” — J. Settings.
- **button** “إيقاف” — J. Settings.

### `admin/shareholders.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “تصدير السجل” — G. Export.

### `admin/tasks.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **input** “بحث في المهام...” — F. Current-page search/filter.
- **button** “مهمة جديدة” — C. Create (business schema).
- **button** “تصفية” — F. Filter.

### `admin/users.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “مجلس الإدارة” — A. Native navigation.
- **a** “اللجان المنبثقة” — A. Native navigation.
- **a** “الجمعية العامة” — A. Native navigation.
- **a** “المساهمين” — A. Native navigation.
- **a** “المالية” — A. Native navigation.
- **a** “الموارد البشرية” — A. Native navigation.
- **a** “تقنية المعلومات” — A. Native navigation.
- **a** “المشتريات” — A. Native navigation.
- **a** “المراجعة الداخلية” — A. Native navigation.
- **a** “الامتثال والمخاطر” — A. Native navigation.
- **a** “السياسات واللوائح” — A. Native navigation.
- **a** “جدول الصلاحيات (DOA)” — A. Native navigation.
- **a** “المهام” — A. Native navigation.
- **a** “التعاميم” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “المستخدمين” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة العليا بحر العرب” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **input** “بحث عن مستخدم...” — F. Current-page search/filter.
- **button** “مستخدم جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — D. Edit.
- **button** “[icon]” — E. Workflow action.
- **button** “[icon]” — D. Edit.
- **button** “[icon]” — E. Workflow action.
- **button** “[icon]” — D. Edit.
- **button** “[icon]” — E. Workflow action.
- **button** “[icon]” — D. Edit.
- **button** “[icon]” — E. Workflow action.
- **button** “[icon]” — D. Edit.
- **button** “[icon]” — E. Workflow action.
- **button** “[icon]” — E. Workflow action.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `audit/audit_plan.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “خطة المراجعة السنوية” — A. Native navigation.
- **a** “أوراق العمل والمهمات” — A. Native navigation.
- **a** “الملاحظات (Observations) 8” — A. Native navigation.
- **a** “سجل المخاطر (Risk Register)” — A. Native navigation.
- **a** “تقارير المراجعة” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “المراجعة الداخلية Chief Audit Exec” — A. Native navigation.
- **button** “تصدير الخطة” — G. Export.
- **button** “إضافة مهمة جديدة” — C. Create (business schema).
- **input** “البحث برقم المهمة، الإدارة، أو المراجع...” — F. Current-page search/filter.
- **select** “عام 2026 عام 2025” — F. Native selection / table filter.
- **select** “جميع الأرباع الربع الأول (Q1) الربع الثاني (Q2) الربع الثالث (Q3) الربع الرابع (Q4)” — F. Native selection / table filter.
- **select** “جميع الحالات مجدولة (لم تبدأ) تخطيط (Planning) قيد التنفيذ (Fieldwork) إصدار التقرير (Reporting) مكتملة (Completed)” — F. Native selection / table filter.
- **button** “إدارة المهمة وأوراق العمل” — H. Download / preview.
- **button** “تعديل” — D. Edit.
- **button** “إدارة المهمة وأوراق العمل” — H. Download / preview.
- **button** “تعديل” — D. Edit.
- **button** “إدارة المهمة وأوراق العمل” — H. Download / preview.
- **button** “تعديل” — D. Edit.
- **button** “عرض التقرير النهائي” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `audit/audit_reports.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “خطة المراجعة السنوية” — A. Native navigation.
- **a** “أوراق العمل والمهمات” — A. Native navigation.
- **a** “الملاحظات (Observations) 8” — A. Native navigation.
- **a** “سجل المخاطر (Risk Register)” — A. Native navigation.
- **a** “تقارير المراجعة” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “المراجعة الداخلية Chief Audit Exec” — A. Native navigation.
- **button** “ملخص ربع سنوي” — H. Download / preview.
- **button** “صياغة تقرير جديد” — D. Edit.
- **input** “البحث برقم التقرير، اسم الإدارة، أو التقييم العام...” — F. Current-page search/filter.
- **select** “التقييم العام (Rating) مرضٍ (Satisfactory) يحتاج تحسين (Needs Imprv) غير مرضٍ (Unsatisfactory)” — F. Native selection / table filter.
- **select** “حالة التقرير مسودة (Draft) بانتظار رد الإدارة معروض على اللجنة نهائي مُصدر (Final Issued)” — F. Native selection / table filter.
- **button** “استعراض المسودة” — H. Download / preview.
- **button** “إدخال رد الإدارة” — E. Workflow action.
- **button** “عرض التقرير النهائي” — H. Download / preview.
- **button** “متابعة الخطة التصحيحية (CAP)” — E. Workflow action.
- **button** “تحميل PDF” — G. Export.
- **button** “تحميل PDF” — G. Export.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `audit/index.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “خطة المراجعة السنوية” — A. Native navigation.
- **a** “أوراق العمل والمهمات” — A. Native navigation.
- **a** “الملاحظات (Observations) 8” — A. Native navigation.
- **a** “سجل المخاطر (Risk Register)” — A. Native navigation.
- **a** “تقارير المراجعة” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “المراجعة الداخلية Chief Audit Executive” — A. Native navigation.
- **a** “عرض خطة المراجعة” — A. Native navigation.
- **a** “التفاصيل” — A. Native navigation.
- **a** “سجل الملاحظات” — A. Native navigation.

### `audit/observations.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “خطة المراجعة السنوية” — A. Native navigation.
- **a** “أوراق العمل والمهمات” — A. Native navigation.
- **a** “الملاحظات (Observations) 8” — A. Native navigation.
- **a** “سجل المخاطر (Risk Register)” — A. Native navigation.
- **a** “تقارير المراجعة” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “المراجعة الداخلية Chief Audit Exec” — A. Native navigation.
- **button** “تصدير التقرير” — G. Export.
- **button** “تسجيل ملاحظة جديدة” — C. Create (business schema).
- **input** “البحث برقم الملاحظة، العنوان، أو الإدارة المعنية...” — F. Current-page search/filter.
- **select** “جميع مستويات الخطر عالٍ (High) متوسط (Medium) منخفض (Low)” — F. Native selection / table filter.
- **select** “جميع الحالات مفتوحة (قيد العمل) متأخرة (Overdue) بانتظار التحقق (Pending Verification) مغلقة (Closed)” — F. Native selection / table filter.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “إرسال تذكير تصعيدي (Escalation)” — E. Workflow action.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “متابعة الـ CAP” — E. Workflow action.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “تحقق وإغلاق” — E. Workflow action.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “متابعة الـ CAP” — E. Workflow action.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `audit/profile.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “خطة المراجعة السنوية” — A. Native navigation.
- **a** “أوراق العمل والمهمات” — A. Native navigation.
- **a** “الملاحظات (Observations) 8” — A. Native navigation.
- **a** “سجل المخاطر (Risk Register)” — A. Native navigation.
- **a** “تقارير المراجعة” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “المراجعة الداخلية Chief Audit Exec” — A. Native navigation.

### `audit/risk_reports.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “خطة المراجعة السنوية” — A. Native navigation.
- **a** “أوراق العمل والمهمات” — A. Native navigation.
- **a** “الملاحظات (Observations) 8” — A. Native navigation.
- **a** “سجل المخاطر (Risk Register)” — A. Native navigation.
- **a** “تقارير المراجعة” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “المراجعة الداخلية Chief Audit Exec” — A. Native navigation.
- **button** “مصفوفة المخاطر (Matrix)” — E. Workflow action.
- **button** “تعريف خطر جديد” — C. Create (business schema).
- **input** “البحث برقم الخطر، الوصف، أو مالك الخطر...” — F. Current-page search/filter.
- **select** “جميع التصنيفات استراتيجية (Strategic) تشغيلية (Operational) مالية (Financial) تقنية / سيبرانية (IT/Cyber) امتثال (Compli” — F. Native selection / table filter.
- **select** “جميع مستويات الخطر حرج (Critical) عالٍ (High) متوسط (Medium) منخفض (Low)” — F. Native selection / table filter.
- **button** “استعراض الخطة” — H. Download / preview.
- **button** “تحديث التقييم” — E. Workflow action.
- **button** “استعراض الخطة” — H. Download / preview.
- **button** “تحديث التقييم” — E. Workflow action.
- **button** “استعراض الخطة” — H. Download / preview.
- **button** “تحديث التقييم” — E. Workflow action.
- **button** “استعراض الخطة” — H. Download / preview.
- **button** “تحديث التقييم” — E. Workflow action.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `audit/working_papers.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “خطة المراجعة السنوية” — A. Native navigation.
- **a** “أوراق العمل والمهمات” — A. Native navigation.
- **a** “الملاحظات (Observations) 8” — A. Native navigation.
- **a** “سجل المخاطر (Risk Register)” — A. Native navigation.
- **a** “تقارير المراجعة” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “المراجعة الداخلية Chief Audit Exec” — A. Native navigation.
- **button** “تحميل القوالب” — H. Download / preview.
- **button** “إنشاء ورقة عمل” — C. Create (business schema).
- **input** “البحث برقم ورقة العمل، المهمة، أو المراجع...” — F. Current-page search/filter.
- **select** “جميع المهام (Engagements) AUD-26-012: مراجعة المبيعات والتسويق AUD-26-013: مراجعة الأصول الثابتة AUD-26-014: مراجعة مسير” — F. Native selection / table filter.
- **select** “حالة ورقة العمل مسودة (Draft) قيد المراجعة (In Review) معتمدة (Approved) معادة (Returned)” — F. Native selection / table filter.
- **button** “مراجعة واعتماد” — E. Workflow action.
- **button** “عرض التعليقات” — H. Download / preview.
- **button** “تعديل الورقة” — D. Edit.
- **button** “استعراض فقط” — H. Download / preview.
- **button** “استكمال التحرير” — D. Edit.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `board/communication.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاجتماعات والقرارات 1” — A. Native navigation.
- **a** “التعاميم والتواصل” — A. Native navigation.
- **a** “التقارير المالية” — A. Native navigation.
- **a** “الحوكمة والامتثال” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “لوحة الإدارة التنفيذية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. عبد الله الحواس رئيس مجلس الإدارة” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “توجيه تعميم للأعضاء” — I. Communication.
- **a** “تحميل المرفق (PDF)” — K. Placeholder link; backend or route configuration required.
- **a** “تحميل القرار” — K. Placeholder link; backend or route configuration required.
- **input** “مثال: إدراج بند في جدول الأعمال” — Form field; page-specific form submission or backend integration.
- **textarea** “اكتب الملاحظة هنا...” — Form field; page-specific form submission or backend integration.
- **button** “إرسال لأمانة السر” — J. Settings.

### `board/finance.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاجتماعات والقرارات 1” — A. Native navigation.
- **a** “التعاميم والتواصل” — A. Native navigation.
- **a** “التقارير المالية” — A. Native navigation.
- **a** “الحوكمة والامتثال” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “لوحة الإدارة التنفيذية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. عبد الله الحواس رئيس مجلس الإدارة” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “تحميل القوائم المدققة (Q3)” — H. Download / preview.
- **button** “اعتماد وتوقيع” — E. Workflow action.
- **button** “تحميل الملف” — H. Download / preview.
- **button** “تحميل الملف” — H. Download / preview.

### `board/governance.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاجتماعات والقرارات 1” — A. Native navigation.
- **a** “التعاميم والتواصل” — A. Native navigation.
- **a** “التقارير المالية” — A. Native navigation.
- **a** “الحوكمة والامتثال” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “لوحة الإدارة التنفيذية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. عبد الله الحواس رئيس مجلس الإدارة” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “تقرير الحوكمة السنوي” — H. Download / preview.
- **button** “[icon]” — H. Download / preview.
- **button** “[icon]” — H. Download / preview.
- **button** “[icon]” — H. Download / preview.
- **button** “استعراض التقرير المعتمد (PDF)” — G. Export.

### `board/index.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاجتماعات والقرارات 1” — A. Native navigation.
- **a** “التعاميم والتواصل” — A. Native navigation.
- **a** “التقارير المالية” — A. Native navigation.
- **a** “الحوكمة والامتثال” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “لوحة الإدارة التنفيذية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. عبد الله الحواس رئيس مجلس الإدارة” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **a** “كل الاجتماعات” — A. Native navigation.
- **button** “استعراض المحاضر السابقة” — H. Download / preview.
- **button** “الاطلاع على حقيبة الاجتماع” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “اعتماد وتوقيع المحضر” — E. Workflow action.
- **a** “عرض التقرير المرفق” — A. Native navigation.

### `board/meetings.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاجتماعات والقرارات 1” — A. Native navigation.
- **a** “التعاميم والتواصل” — A. Native navigation.
- **a** “التقارير المالية” — A. Native navigation.
- **a** “الحوكمة والامتثال” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “لوحة الإدارة التنفيذية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. عبد الله الحواس رئيس مجلس الإدارة” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “التقويم السنوي” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “استعراض المسودة” — H. Download / preview.
- **button** “إضافة ملاحظة” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “توقيع إلكتروني واعتماد” — E. Workflow action.
- **button** “حقيبة الاجتماع” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “رابط الحضور” — E. Workflow action.
- **select** “عام 2026 عام 2025” — F. Native selection / table filter.
- **button** “عرض المحضر” — H. Download / preview.
- **button** “حقيبة الاجتماع” — H. Download / preview.
- **button** “عرض المحضر” — H. Download / preview.
- **button** “حقيبة الاجتماع” — H. Download / preview.

### `board/profile.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاجتماعات والقرارات 1” — A. Native navigation.
- **a** “التعاميم والتواصل” — A. Native navigation.
- **a** “التقارير المالية” — A. Native navigation.
- **a** “الحوكمة والامتثال” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “لوحة الإدارة التنفيذية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. عبد الله الحواس رئيس مجلس الإدارة” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.

### `ceo/ceo_broadcast.html`

- **a** “الرئيسية (نظرة عامة)” — A. Native navigation.
- **a** “الخطة الاستراتيجية” — A. Native navigation.
- **a** “المؤشرات المالية” — A. Native navigation.
- **a** “تقارير الأداء التنفيذي” — A. Native navigation.
- **a** “الحوكمة والسياسات” — A. Native navigation.
- **a** “إدارة المخاطر” — A. Native navigation.
- **a** “البث والتعاميم الإدارية” — A. Native navigation.
- **a** “التواصل والاجتماعات” — A. Native navigation.
- **a** “المرئيات والملاحظات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “التحويل للوحة الإدارية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. هيثم بن محمد السحيباني الرئيس التنفيذي (CEO)” — A. Native navigation.
- **select** “كافة منسوبي الشركة (عام) قطاع العمليات التجارية (المبيعات والتسويق) قطاع العمليات التقنية (تطوير النظم والتشغيل) مدريري ” — F. Native selection / table filter.
- **input** “عنوان التوجيه الإداري...” — Form field; page-specific form submission or backend integration.
- **textarea** “اكتب نص القرار التنفيذي هنا...” — Form field; page-specific form submission or backend integration.
- **input** “يتطلب التوقيع بالعلم الإلكتروني من المستهدفين” — Form field; page-specific form submission or backend integration.
- **button** “نشر وتعميم القرار فوراً” — I. Communication.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “عرض التفاصيل” — H. Download / preview.

### `ceo/ceo_communication.html`

- **a** “الرئيسية (نظرة عامة)” — A. Native navigation.
- **a** “الخطة الاستراتيجية” — A. Native navigation.
- **a** “المؤشرات المالية” — A. Native navigation.
- **a** “تقارير الأداء التنفيذي” — A. Native navigation.
- **a** “الحوكمة والسياسات” — A. Native navigation.
- **a** “إدارة المخاطر” — A. Native navigation.
- **a** “البث والتعاميم الإدارية” — A. Native navigation.
- **a** “التواصل والاجتماعات” — A. Native navigation.
- **a** “المرئيات والملاحظات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “التحويل للوحة الإدارية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. هيثم بن محمد السحيباني الرئيس التنفيذي (CEO)” — A. Native navigation.
- **button** “جدولة اجتماع قيادي جديد” — C. Create (business schema).
- **button** “الانضمام للأنظمة” — A. Navigation.
- **button** “حقيبة الاجتماع” — K. Backend-dependent (explicit explanation; no fake completion).
- **a** “تعميم إداري للقطاعات” — A. Native navigation.
- **a** “محادثة مع أمانة سر المجلس” — A. Native navigation.

### `ceo/ceo_feedback.html`

- **a** “الرئيسية (نظرة عامة)” — A. Native navigation.
- **a** “الخطة الاستراتيجية” — A. Native navigation.
- **a** “المؤشرات المالية” — A. Native navigation.
- **a** “تقارير الأداء التنفيذي” — A. Native navigation.
- **a** “الحوكمة والسياسات” — A. Native navigation.
- **a** “إدارة المخاطر” — A. Native navigation.
- **a** “البث والتعاميم الإدارية” — A. Native navigation.
- **a** “التواصل والاجتماعات” — A. Native navigation.
- **a** “المرئيات والملاحظات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “التحويل للوحة الإدارية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. هيثم بن محمد السحيباني الرئيس التنفيذي (CEO)” — A. Native navigation.
- **button** “موافقة وتوجيه للمالية” — E. Workflow action.
- **button** “إعادة للمراجعة” — E. Workflow action.
- **button** “اعتماد وإحالة للمشتريات” — E. Workflow action.
- **button** “حفظ في الأرشيف” — J. Settings.

### `ceo/ceo_finance.html`

- **a** “الرئيسية (نظرة عامة)” — A. Native navigation.
- **a** “الخطة الاستراتيجية” — A. Native navigation.
- **a** “المؤشرات المالية” — A. Native navigation.
- **a** “تقارير الأداء التنفيذي” — A. Native navigation.
- **a** “الحوكمة والسياسات” — A. Native navigation.
- **a** “إدارة المخاطر” — A. Native navigation.
- **a** “البث والتعاميم الإدارية” — A. Native navigation.
- **a** “التواصل والاجتماعات” — A. Native navigation.
- **a** “المرئيات والملاحظات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “التحويل للوحة الإدارية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. هيثم بن محمد السحيباني الرئيس التنفيذي (CEO)” — A. Native navigation.
- **button** “تصدير الموازنة العامة (PDF)” — G. Export.

### `ceo/ceo_governance.html`

- **a** “الرئيسية (نظرة عامة)” — A. Native navigation.
- **a** “الخطة الاستراتيجية” — A. Native navigation.
- **a** “المؤشرات المالية” — A. Native navigation.
- **a** “تقارير الأداء التنفيذي” — A. Native navigation.
- **a** “الحوكمة والسياسات” — A. Native navigation.
- **a** “إدارة المخاطر” — A. Native navigation.
- **a** “البث والتعاميم الإدارية” — A. Native navigation.
- **a** “التواصل والاجتماعات” — A. Native navigation.
- **a** “المرئيات والملاحظات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “التحويل للوحة الإدارية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. هيثم بن محمد السحيباني الرئيس التنفيذي (CEO)” — A. Native navigation.
- **a** “استعراض مصفوفة الصلاحيات (DOA)” — A. Native navigation.
- **button** “تحميل الدليل” — H. Download / preview.
- **button** “تحميل الدليل” — H. Download / preview.
- **button** “تحميل الدليل” — H. Download / preview.

### `ceo/ceo_reports.html`

- **a** “الرئيسية (نظرة عامة)” — A. Native navigation.
- **a** “الخطة الاستراتيجية” — A. Native navigation.
- **a** “المؤشرات المالية” — A. Native navigation.
- **a** “تقارير الأداء التنفيذي” — A. Native navigation.
- **a** “الحوكمة والسياسات” — A. Native navigation.
- **a** “إدارة المخاطر” — A. Native navigation.
- **a** “البث والتعاميم الإدارية” — A. Native navigation.
- **a** “التواصل والاجتماعات” — A. Native navigation.
- **a** “المرئيات والملاحظات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “التحويل للوحة الإدارية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. هيثم بن محمد السحيباني الرئيس التنفيذي (CEO)” — A. Native navigation.
- **button** “طلب تقرير خاص” — C. Create (business schema).
- **button** “عرض التقرير (PDF)” — G. Export.
- **button** “عرض التقرير (PDF)” — G. Export.
- **button** “عرض التقرير (PDF)” — G. Export.
- **button** “عرض التقرير (PDF)” — G. Export.

### `ceo/ceo_risks.html`

- **a** “الرئيسية (نظرة عامة)” — A. Native navigation.
- **a** “الخطة الاستراتيجية” — A. Native navigation.
- **a** “المؤشرات المالية” — A. Native navigation.
- **a** “تقارير الأداء التنفيذي” — A. Native navigation.
- **a** “الحوكمة والسياسات” — A. Native navigation.
- **a** “إدارة المخاطر” — A. Native navigation.
- **a** “البث والتعاميم الإدارية” — A. Native navigation.
- **a** “التواصل والاجتماعات” — A. Native navigation.
- **a** “المرئيات والملاحظات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “التحويل للوحة الإدارية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. هيثم بن محمد السحيباني الرئيس التنفيذي (CEO)” — A. Native navigation.
- **button** “إضافة خطر جديد للسجل” — C. Create (business schema).

### `ceo/ceo_strategy.html`

- **a** “الرئيسية (نظرة عامة)” — A. Native navigation.
- **a** “الخطة الاستراتيجية” — A. Native navigation.
- **a** “المؤشرات المالية” — A. Native navigation.
- **a** “تقارير الأداء التنفيذي” — A. Native navigation.
- **a** “الحوكمة والسياسات” — A. Native navigation.
- **a** “إدارة المخاطر” — A. Native navigation.
- **a** “البث والتعاميم الإدارية” — A. Native navigation.
- **a** “التواصل والاجتماعات” — A. Native navigation.
- **a** “المرئيات والملاحظات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “التحويل للوحة الإدارية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. هيثم بن محمد السحيباني الرئيس التنفيذي (CEO)” — A. Native navigation.
- **button** “تحديث المستهدفات” — D. Edit.

### `ceo/index.html`

- **a** “الرئيسية (نظرة عامة)” — A. Native navigation.
- **a** “الخطة الاستراتيجية” — A. Native navigation.
- **a** “المؤشرات المالية” — A. Native navigation.
- **a** “تقارير الأداء التنفيذي” — A. Native navigation.
- **a** “الحوكمة والسياسات” — A. Native navigation.
- **a** “إدارة المخاطر” — A. Native navigation.
- **a** “البث والتعاميم الإدارية” — A. Native navigation.
- **a** “التواصل والاجتماعات” — A. Native navigation.
- **a** “المرئيات والملاحظات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “التحويل للوحة الإدارية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. هيثم بن محمد السحيباني الرئيس التنفيذي (CEO)” — A. Native navigation.
- **a** “إرسال تعميم تنفيذي” — A. Native navigation.
- **button** “اعتماد” — E. Workflow action.
- **button** “مراجعة” — E. Workflow action.
- **button** “اعتماد” — E. Workflow action.
- **button** “مراجعة” — E. Workflow action.
- **button** “اعتماد” — E. Workflow action.
- **button** “مراجعة” — E. Workflow action.
- **a** “قطاع العمليات التجارية المبيعات، التسويق، التدريب، نجاحات العملاء” — A. Native navigation.
- **a** “قطاع العمليات التقنية تطوير النظم، تشغيل الأنظمة والدعم الفني” — A. Native navigation.
- **a** “متابعة سجل المخاطر المخاطر التشغيلية والمالية والتقنية” — A. Native navigation.

### `ceo/profile.html`

- **a** “الرئيسية (نظرة عامة)” — A. Native navigation.
- **a** “الخطة الاستراتيجية” — A. Native navigation.
- **a** “المؤشرات المالية” — A. Native navigation.
- **a** “تقارير الأداء التنفيذي” — A. Native navigation.
- **a** “الحوكمة والسياسات” — A. Native navigation.
- **a** “إدارة المخاطر” — A. Native navigation.
- **a** “البث والتعاميم الإدارية” — A. Native navigation.
- **a** “التواصل والاجتماعات” — A. Native navigation.
- **a** “المرئيات والملاحظات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “التحويل للوحة الإدارية” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “أ. هيثم بن محمد السحيباني الرئيس التنفيذي (CEO)” — A. Native navigation.

### `cto/cto_assets.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الخوادم (Servers)” — A. Native navigation.
- **a** “مراقبة الشبكة” — A. Native navigation.
- **a** “مركز العمليات (SOC)” — A. Native navigation.
- **a** “إدارة الهويات (IAM)” — A. Native navigation.
- **a** “نظام السنترال” — A. Native navigation.
- **a** “التحويلات الداخلية” — A. Native navigation.
- **a** “سجل المكالمات (CDR)” — A. Native navigation.
- **a** “المشاريع التقنية” — A. Native navigation.
- **a** “أصول تقنية المعلومات” — A. Native navigation.
- **a** “الدعم الفني (Helpdesk) 12” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة التقنية Chief Tech Officer” — A. Native navigation.
- **button** “طباعة ملصقات QR” — G. Export.
- **button** “تسجيل أصل جديد” — C. Create (business schema).
- **input** “البحث برقم الأصل (Tag ID)، الرقم التسلسلي (S/N)، أو الموظف...” — F. Current-page search/filter.
- **select** “جميع فئات الأصول أجهزة محددة (Laptops) حواسب مكتبية (Desktops) أجهزة شبكة (Network/Servers) طابعات وملحقات” — F. Native selection / table filter.
- **select** “جميع الحالات مخصص (Assigned) في المستودع (In Stock) صيانة (Maintenance) مستبعد (Retired)” — F. Native selection / table filter.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “طباعة باركود” — G. Export.
- **button** “تسليم لموظف” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “تجديد الضمان” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `cto/cto_call_logs.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الخوادم (Servers)” — A. Native navigation.
- **a** “مراقبة الشبكة” — A. Native navigation.
- **a** “مركز العمليات (SOC)” — A. Native navigation.
- **a** “إدارة الهويات (IAM)” — A. Native navigation.
- **a** “نظام السنترال” — A. Native navigation.
- **a** “التحويلات الداخلية” — A. Native navigation.
- **a** “سجل المكالمات (CDR)” — A. Native navigation.
- **a** “المشاريع التقنية” — A. Native navigation.
- **a** “أصول تقنية المعلومات” — A. Native navigation.
- **a** “الدعم الفني (Helpdesk) 12” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة التقنية Chief Tech Officer” — A. Native navigation.
- **button** “تصدير (CSV)” — G. Export.
- **button** “تصفية متقدمة” — F. Filter.
- **input** “البحث برقم المتصل، المستقبل، أو التحويلة...” — F. Current-page search/filter.
- **input** “كل أنواع المكالمات صادرة (Outbound) واردة (Inbound) داخلية (Internal)” — Form field; page-specific form submission or backend integration.
- **select** “كل أنواع المكالمات صادرة (Outbound) واردة (Inbound) داخلية (Internal)” — F. Native selection / table filter.
- **button** “استماع للتسجيل” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “التفاصيل المالية” — H. Download / preview.
- **button** “إرسال تنبيه بالبريد” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `cto/cto_extensions.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الخوادم (Servers)” — A. Native navigation.
- **a** “مراقبة الشبكة” — A. Native navigation.
- **a** “مركز العمليات (SOC)” — A. Native navigation.
- **a** “إدارة الهويات (IAM)” — A. Native navigation.
- **a** “نظام السنترال” — A. Native navigation.
- **a** “التحويلات الداخلية” — A. Native navigation.
- **a** “سجل المكالمات (CDR)” — A. Native navigation.
- **a** “المشاريع التقنية” — A. Native navigation.
- **a** “أصول تقنية المعلومات” — A. Native navigation.
- **a** “الدعم الفني (Helpdesk) 12” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة التقنية Chief Tech Officer” — A. Native navigation.
- **button** “تصدير الدليل” — G. Export.
- **button** “إضافة تحويلة” — I. Communication.
- **input** “البحث برقم التحويلة، اسم الموظف، أو رقم الـ MAC...” — F. Current-page search/filter.
- **select** “جميع الإدارات الإدارة التنفيذية المبيعات (Sales) الدعم الفني (IT Support) المالية والموارد البشرية” — F. Native selection / table filter.
- **select** “جميع الحالات (Status) متصل (Registered) غير متصل (Unregistered) ممنوع الاتصال الخارجي” — F. Native selection / table filter.
- **button** “إعدادات التحويلة” — J. Settings.
- **button** “إعدادات التحويلة” — J. Settings.
- **button** “إدارة المجموعة” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “إعدادات التحويلة” — J. Settings.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `cto/cto_iam.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الخوادم (Servers)” — A. Native navigation.
- **a** “مراقبة الشبكة” — A. Native navigation.
- **a** “مركز العمليات (SOC)” — A. Native navigation.
- **a** “إدارة الهويات (IAM)” — A. Native navigation.
- **a** “نظام السنترال” — A. Native navigation.
- **a** “التحويلات الداخلية” — A. Native navigation.
- **a** “سجل المكالمات (CDR)” — A. Native navigation.
- **a** “المشاريع التقنية” — A. Native navigation.
- **a** “أصول تقنية المعلومات” — A. Native navigation.
- **a** “الدعم الفني (Helpdesk) 12” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة التقنية Chief Tech Officer” — A. Native navigation.
- **button** “تقرير الصلاحيات (CSV)” — G. Export.
- **button** “إضافة مستخدم” — C. Create (business schema).
- **input** “البحث باسم المستخدم، البريد، أو المسمى الوظيفي...” — F. Current-page search/filter.
- **select** “جميع الإدارات الإدارة التنفيذية الإدارة المالية الموارد البشرية تقنية المعلومات” — F. Native selection / table filter.
- **select** “حالة الحساب نشط (Active) موقوف مؤقتاً (Suspended) مقفل (Locked) بانتظار الإعداد” — F. Native selection / table filter.
- **button** “إدارة الصلاحيات” — J. Settings.
- **button** “فك القفل (Unlock)” — E. Workflow action.
- **button** “إعادة تعيين كلمة المرور” — D. Edit.
- **button** “إرسال رابط التفعيل” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “حذف نهائي” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `cto/cto_monitoring.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الخوادم (Servers)” — A. Native navigation.
- **a** “مراقبة الشبكة” — A. Native navigation.
- **a** “مركز العمليات (SOC)” — A. Native navigation.
- **a** “إدارة الهويات (IAM)” — A. Native navigation.
- **a** “نظام السنترال” — A. Native navigation.
- **a** “التحويلات الداخلية” — A. Native navigation.
- **a** “سجل المكالمات (CDR)” — A. Native navigation.
- **a** “المشاريع التقنية” — A. Native navigation.
- **a** “أصول تقنية المعلومات” — A. Native navigation.
- **a** “الدعم الفني (Helpdesk) 12” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة التقنية Chief Tech Officer” — A. Native navigation.
- **button** “تقرير الأداء (SLA)” — H. Download / preview.
- **button** “إضافة نقطة مراقبة” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “تحديث” — E. Workflow action.
- **button** “إخفاء الكل” — F. Filter.

### `cto/cto_pbx.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الخوادم (Servers)” — A. Native navigation.
- **a** “مراقبة الشبكة” — A. Native navigation.
- **a** “مركز العمليات (SOC)” — A. Native navigation.
- **a** “إدارة الهويات (IAM)” — A. Native navigation.
- **a** “نظام السنترال” — A. Native navigation.
- **a** “التحويلات الداخلية” — A. Native navigation.
- **a** “سجل المكالمات (CDR)” — A. Native navigation.
- **a** “المشاريع التقنية” — A. Native navigation.
- **a** “أصول تقنية المعلومات” — A. Native navigation.
- **a** “الدعم الفني (Helpdesk) 12” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة التقنية Chief Tech Officer” — A. Native navigation.
- **button** “إعادة تشغيل الخدمة” — E. Workflow action.
- **button** “إضافة خط جديد (Trunk)” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “البحث باسم الخط، مزود الخدمة، أو الـ IP...” — F. Current-page search/filter.
- **select** “حالة الخط (Trunk Status) متصل (Registered) غير متصل (Unregistered) تحذير (Warning)” — F. Native selection / table filter.
- **button** “إعدادات الخط” — J. Settings.
- **button** “إعدادات الخط” — J. Settings.
- **button** “إعدادات الخط” — J. Settings.
- **button** “إعادة الاتصال (Reconnect)” — E. Workflow action.
- **button** “إعدادات الخط” — J. Settings.

### `cto/cto_projects.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الخوادم (Servers)” — A. Native navigation.
- **a** “مراقبة الشبكة” — A. Native navigation.
- **a** “مركز العمليات (SOC)” — A. Native navigation.
- **a** “إدارة الهويات (IAM)” — A. Native navigation.
- **a** “نظام السنترال” — A. Native navigation.
- **a** “التحويلات الداخلية” — A. Native navigation.
- **a** “سجل المكالمات (CDR)” — A. Native navigation.
- **a** “المشاريع التقنية” — A. Native navigation.
- **a** “أصول تقنية المعلومات” — A. Native navigation.
- **a** “الدعم الفني (Helpdesk) 12” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة التقنية Chief Tech Officer” — A. Native navigation.
- **button** “مخطط جانت (Gantt)” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “مشروع جديد” — C. Create (business schema).
- **input** “البحث باسم المشروع، مدير المشروع، أو التقنية المستخدمة...” — F. Current-page search/filter.
- **select** “جميع التصنيفات بنية تحتية (Infrastructure) أمن سيبراني (Cybersecurity) أنظمة وتطبيقات (Software)” — F. Native selection / table filter.
- **select** “جميع الحالات قيد التنفيذ (In Progress) مكتمل (Completed) متأخر (Delayed)” — F. Native selection / table filter.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “عرض التفاصيل” — H. Download / preview.

### `cto/cto_servers.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الخوادم (Servers)” — A. Native navigation.
- **a** “مراقبة الشبكة” — A. Native navigation.
- **a** “مركز العمليات (SOC)” — A. Native navigation.
- **a** “إدارة الهويات (IAM)” — A. Native navigation.
- **a** “نظام السنترال” — A. Native navigation.
- **a** “التحويلات الداخلية” — A. Native navigation.
- **a** “سجل المكالمات (CDR)” — A. Native navigation.
- **a** “المشاريع التقنية” — A. Native navigation.
- **a** “أصول تقنية المعلومات” — A. Native navigation.
- **a** “الدعم الفني (Helpdesk) 12” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة التقنية Chief Tech Officer” — A. Native navigation.
- **button** “تصدير (CSV)” — G. Export.
- **button** “إضافة خادم جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “البحث باسم الخادم، عنوان الـ IP، نظام التشغيل...” — F. Current-page search/filter.
- **select** “جميع البيئات (Environments) الإنتاج (Production) التطوير (Development) الاختبار (Staging)” — F. Native selection / table filter.
- **select** “حالة الخادم يعمل (Online) تحذير (Warning) متوقف (Offline) صيانة (Maintenance)” — F. Native selection / table filter.
- **button** “استعراض الموارد” — H. Download / preview.
- **button** “إعدادات (vSphere)” — J. Settings.
- **button** “استعراض الموارد” — H. Download / preview.
- **button** “إعدادات (vSphere)” — J. Settings.
- **button** “استعراض الموارد” — H. Download / preview.
- **button** “إعدادات (vSphere)” — J. Settings.
- **button** “تشغيل (Power On)” — E. Workflow action.
- **button** “إعدادات (vSphere)” — J. Settings.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `cto/cto_soc.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الخوادم (Servers)” — A. Native navigation.
- **a** “مراقبة الشبكة” — A. Native navigation.
- **a** “مركز العمليات (SOC)” — A. Native navigation.
- **a** “إدارة الهويات (IAM)” — A. Native navigation.
- **a** “نظام السنترال” — A. Native navigation.
- **a** “التحويلات الداخلية” — A. Native navigation.
- **a** “سجل المكالمات (CDR)” — A. Native navigation.
- **a** “المشاريع التقنية” — A. Native navigation.
- **a** “أصول تقنية المعلومات” — A. Native navigation.
- **a** “الدعم الفني (Helpdesk) 12” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة التقنية Chief Tech Officer” — A. Native navigation.
- **button** “تقرير التهديدات (PDF)” — G. Export.
- **button** “فحص شامل (Vulnerability Scan)” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “البحث برقم الحدث (Event ID)، الـ IP، أو نوع التهديد...” — F. Current-page search/filter.
- **select** “جميع مستويات الخطر حرج (Critical) عالٍ (High) متوسط (Medium) منخفض (Low)” — F. Native selection / table filter.
- **select** “جميع الحالات نشط (تحت المعالجة) تم الحظر (Blocked) تم الاحتواء (Mitigated) إنذار كاذب (False Positive)” — F. Native selection / table filter.
- **button** “تفاصيل” — H. Download / preview.
- **button** “تفاصيل” — H. Download / preview.
- **button** “عزل (Isolate)” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “تفاصيل” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `cto/cto_support.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الخوادم (Servers)” — A. Native navigation.
- **a** “مراقبة الشبكة” — A. Native navigation.
- **a** “مركز العمليات (SOC)” — A. Native navigation.
- **a** “إدارة الهويات (IAM)” — A. Native navigation.
- **a** “نظام السنترال” — A. Native navigation.
- **a** “التحويلات الداخلية” — A. Native navigation.
- **a** “سجل المكالمات (CDR)” — A. Native navigation.
- **a** “المشاريع التقنية” — A. Native navigation.
- **a** “أصول تقنية المعلومات” — A. Native navigation.
- **a** “الدعم الفني (Helpdesk) 12” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة التقنية Chief Tech Officer” — A. Native navigation.
- **button** “تقرير الأداء” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “إنشاء تذكرة جديدة” — C. Create (business schema).
- **input** “البحث برقم التذكرة، العنوان، صاحب الطلب، أو المهندس...” — F. Current-page search/filter.
- **select** “جميع التصنيفات مشاكل البرامج (Software) مشاكل العتاد (Hardware) الشبكة والـ VPN البريد الإلكتروني والـ IAM” — F. Native selection / table filter.
- **select** “الأولوية (Priority) عاجل (Urgent) عالي (High) متوسط (Medium) منخفض (Low)” — F. Native selection / table filter.
- **select** “حالة التذكرة جديدة (New) قيد المعالجة (In Progress) مكتملة ومغلقة (Resolved)” — F. Native selection / table filter.
- **button** “عرض التذكرة والرد” — H. Download / preview.
- **button** “عرض التذكرة والرد” — H. Download / preview.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `cto/index.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الخوادم (Servers)” — A. Native navigation.
- **a** “مراقبة الشبكة” — A. Native navigation.
- **a** “مركز العمليات (SOC)” — A. Native navigation.
- **a** “إدارة الهويات (IAM)” — A. Native navigation.
- **a** “نظام السنترال” — A. Native navigation.
- **a** “التحويلات الداخلية” — A. Native navigation.
- **a** “سجل المكالمات (CDR)” — A. Native navigation.
- **a** “المشاريع التقنية” — A. Native navigation.
- **a** “أصول تقنية المعلومات” — A. Native navigation.
- **a** “الدعم الفني (Helpdesk) 12” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة التقنية Chief Tech Officer” — A. Native navigation.
- **a** “شاشة المراقبة” — A. Native navigation.
- **a** “مراقبة تفصيلية” — A. Native navigation.

### `cto/profile.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الخوادم (Servers)” — A. Native navigation.
- **a** “مراقبة الشبكة” — A. Native navigation.
- **a** “مركز العمليات (SOC)” — A. Native navigation.
- **a** “إدارة الهويات (IAM)” — A. Native navigation.
- **a** “نظام السنترال” — A. Native navigation.
- **a** “التحويلات الداخلية” — A. Native navigation.
- **a** “سجل المكالمات (CDR)” — A. Native navigation.
- **a** “المشاريع التقنية” — A. Native navigation.
- **a** “أصول تقنية المعلومات” — A. Native navigation.
- **a** “الدعم الفني (Helpdesk) 12” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة التقنية Chief Tech Officer” — A. Native navigation.

### `employee/approvals.html`

- **a** “الرئيسية” — A. Native navigation.
- **a** “الطلبات الإدارية” — A. Native navigation.
- **a** “الخدمات المالية” — A. Native navigation.
- **a** “الدعم الفني والخدمات” — A. Native navigation.
- **a** “ملفاتي السحابية” — A. Native navigation.
- **a** “الاعتمادات والتواقيع 2” — A. Native navigation.
- **a** “الأداء والتدريب” — A. Native navigation.
- **a** “اللوائح والسياسات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “م. أيمن المغربي مهندس برمجيات” — A. Native navigation.
- **button** “إعداد توقيعي الشخصي” — J. Settings.
- **button** “إنشاء مسار اعتماد جديد” — H. Download / preview.
- **input** “البحث باسم المستند، المرسل، أو التخصص...” — F. Current-page search/filter.
- **select** “جميع الحالات بانتظار توقيعي أرسلتها (قيد الاعتماد) مكتملة الأطراف” — F. Native selection / table filter.
- **button** “توقيع” — D. Edit.
- **button** “رفض وإعادة” — E. Workflow action.
- **button** “إرسال تذكير (Remind)” — A. Navigation / shared shell.
- **button** “عرض المستند” — H. Download / preview.
- **button** “تحميل الشهادة (Audit Trail)” — H. Download / preview.
- **button** “تحميل المستند PDF” — G. Export.
- **button** “قراءة سبب الرفض” — E. Workflow action.
- **button** “إعادة إرسال بعد التعديل” — E. Workflow action.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `employee/cloud.html`

- **a** “الرئيسية” — A. Native navigation.
- **a** “الطلبات الإدارية” — A. Native navigation.
- **a** “الخدمات المالية” — A. Native navigation.
- **a** “الدعم الفني والخدمات” — A. Native navigation.
- **a** “ملفاتي السحابية” — A. Native navigation.
- **a** “الاعتمادات والتواقيع 2” — A. Native navigation.
- **a** “الأداء والتدريب” — A. Native navigation.
- **a** “اللوائح والسياسات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “م. أيمن المغربي مهندس برمجيات” — A. Native navigation.
- **button** “رفع ملفات جديدة” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “مجلد جديد” — H. Download / preview.
- **a** “ملفاتي” — K. Placeholder link; backend or route configuration required.
- **input** “البحث في ملفاتي...” — F. Current-page search/filter.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **button** “تحميل” — H. Download / preview.
- **button** “مشاركة رابط” — I. Communication.
- **button** “حذف” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **button** “تحميل” — H. Download / preview.
- **button** “مشاركة رابط” — I. Communication.
- **button** “حذف” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **button** “تحميل” — H. Download / preview.
- **button** “مشاركة رابط” — I. Communication.
- **button** “حذف” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **button** “تحميل” — H. Download / preview.
- **button** “مشاركة رابط” — I. Communication.
- **button** “حذف” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “تصفح جهازك” — K. Backend-dependent (explicit explanation; no fake completion).

### `employee/finance.html`

- **a** “الرئيسية” — A. Native navigation.
- **a** “الطلبات الإدارية” — A. Native navigation.
- **a** “الخدمات المالية” — A. Native navigation.
- **a** “الدعم الفني والخدمات” — A. Native navigation.
- **a** “ملفاتي السحابية” — A. Native navigation.
- **a** “الاعتمادات والتواقيع 2” — A. Native navigation.
- **a** “الأداء والتدريب” — A. Native navigation.
- **a** “اللوائح والسياسات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “م. أيمن المغربي مهندس برمجيات” — A. Native navigation.
- **button** “طلب عهدة مالية” — C. Create (business schema).
- **button** “مطالبة بمصروفات (Expense)” — C. Create (business schema).
- **input** “البحث برقم المعاملة، الشهر، أو نوع الطلب...” — F. Current-page search/filter.
- **select** “جميع الأنواع مسيرات الرواتب (Payslips) مطالبات المصاريف (Expenses) العهد والتسويات (Petty Cash)” — F. Native selection / table filter.
- **select** “السنة: 2026 السنة: 2025” — F. Native selection / table filter.
- **button** “استعراض التفاصيل” — H. Download / preview.
- **button** “تحميل ملف PDF” — G. Export.
- **button** “استعراض التفاصيل والمرفقات” — H. Download / preview.
- **button** “تسوية” — H. Download / preview.
- **button** “استعراض التفاصيل” — H. Download / preview.
- **button** “تحميل ملف PDF” — G. Export.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `employee/index.html`

- **a** “الرئيسية” — A. Native navigation.
- **a** “الطلبات الإدارية” — A. Native navigation.
- **a** “الخدمات المالية” — A. Native navigation.
- **a** “الدعم الفني والخدمات” — A. Native navigation.
- **a** “ملفاتي السحابية” — A. Native navigation.
- **a** “الاعتمادات والتواقيع 2” — A. Native navigation.
- **a** “الأداء والتدريب” — A. Native navigation.
- **a** “اللوائح والسياسات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “تسجيل دخول (Punch In)” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “م. أيمن المغربي مهندس برمجيات” — A. Native navigation.
- **a** “طلب إجازة” — A. Native navigation.
- **a** “مراجعة واعتماد الآن” — A. Native navigation.
- **a** “الأرشيف” — A. Native navigation.
- **a** “Policy_v2.pdf” — K. Placeholder link; backend or route configuration required.
- **a** “رفع ملف للسحابة (My Drive) مساحتك المتبقية: 4.2 GB” — A. Native navigation.
- **a** “إنشاء مسار اعتماد جديد طلب توقيع مديرك أو زملائك” — A. Native navigation.
- **a** “استعراض مسير راتب (سبتمبر) تم إصداره وإضافته لملفك” — A. Native navigation.
- **a** “فتح تذكرة دعم فني (IT) للإبلاغ عن عطل في جهازك” — A. Native navigation.

### `employee/performance.html`

- **a** “الرئيسية” — A. Native navigation.
- **a** “الطلبات الإدارية” — A. Native navigation.
- **a** “الخدمات المالية” — A. Native navigation.
- **a** “الدعم الفني والخدمات” — A. Native navigation.
- **a** “ملفاتي السحابية” — A. Native navigation.
- **a** “الاعتمادات والتواقيع 2” — A. Native navigation.
- **a** “الأداء والتدريب” — A. Native navigation.
- **a** “اللوائح والسياسات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “م. أيمن المغربي مهندس برمجيات” — A. Native navigation.
- **button** “صياغة هدف جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “منصة التعليم” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “تحديث النسب” — D. Edit.
- **button** “عرض الكتالوج” — H. Download / preview.
- **button** “تحميل الشهادة” — H. Download / preview.
- **button** “متابعة” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “البدء” — K. Backend-dependent (explicit explanation; no fake completion).

### `employee/policies.html`

- **a** “الرئيسية” — A. Native navigation.
- **a** “الطلبات الإدارية” — A. Native navigation.
- **a** “الخدمات المالية” — A. Native navigation.
- **a** “الدعم الفني والخدمات” — A. Native navigation.
- **a** “ملفاتي السحابية” — A. Native navigation.
- **a** “الاعتمادات والتواقيع 2” — A. Native navigation.
- **a** “الأداء والتدريب” — A. Native navigation.
- **a** “اللوائح والسياسات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “م. أيمن المغربي مهندس برمجيات” — A. Native navigation.
- **button** “إقرار القراءة الشاملة” — H. Download / preview.
- **input** “البحث باسم اللائحة، القسم، أو الكلمات المفتاحية...” — F. Current-page search/filter.
- **select** “جميع التصنيفات الموارد البشرية والعمل أمن المعلومات والتقنية السلوك المهني والنزاهة السلامة والصحة المهنية” — F. Native selection / table filter.
- **button** “إقرار بالاطلاع” — E. Workflow action.
- **button** “تحميل المستند PDF” — G. Export.
- **button** “استعراض” — H. Download / preview.
- **button** “تحميل المستند PDF” — G. Export.
- **button** “استعراض” — H. Download / preview.
- **button** “تحميل المستند PDF” — G. Export.
- **button** “استعراض” — H. Download / preview.
- **button** “تحميل المستند PDF” — G. Export.
- **button** “استعراض” — H. Download / preview.
- **button** “تحميل المستند PDF” — G. Export.
- **button** “استعراض” — H. Download / preview.
- **button** “تحميل المستند PDF” — G. Export.

### `employee/profile.html`

- **a** “الرئيسية” — A. Native navigation.
- **a** “الطلبات الإدارية” — A. Native navigation.
- **a** “الخدمات المالية” — A. Native navigation.
- **a** “الدعم الفني والخدمات” — A. Native navigation.
- **a** “ملفاتي السحابية” — A. Native navigation.
- **a** “الاعتمادات والتواقيع 2” — A. Native navigation.
- **a** “الأداء والتدريب” — A. Native navigation.
- **a** “اللوائح والسياسات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “م. أيمن المغربي مهندس برمجيات” — A. Native navigation.
- **button** “تعديل” — D. Edit.
- **button** “[icon]” — D. Edit.
- **button** “طلب تغيير” — K. Backend-dependent (explicit explanation; no fake completion).

### `employee/requests.html`

- **a** “الرئيسية” — A. Native navigation.
- **a** “الطلبات الإدارية” — A. Native navigation.
- **a** “الخدمات المالية” — A. Native navigation.
- **a** “الدعم الفني والخدمات” — A. Native navigation.
- **a** “ملفاتي السحابية” — A. Native navigation.
- **a** “الاعتمادات والتواقيع 2” — A. Native navigation.
- **a** “الأداء والتدريب” — A. Native navigation.
- **a** “اللوائح والسياسات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “م. أيمن المغربي مهندس برمجيات” — A. Native navigation.
- **button** “طلب خطاب تعريف” — H. Download / preview.
- **button** “طلب إجازة جديد” — C. Create (business schema).
- **input** “البحث برقم الطلب أو نوعه...” — F. Current-page search/filter.
- **select** “جميع أنواع الطلبات الإجازات خطابات التعريف الاستئذانات والتأخير” — F. Native selection / table filter.
- **select** “جميع الحالات قيد الاعتماد معتمد / مكتمل مرفوض” — F. Native selection / table filter.
- **button** “إلغاء الطلب” — E. Workflow action.
- **button** “التفاصيل” — H. Download / preview.
- **button** “إلغاء الطلب” — E. Workflow action.
- **button** “التفاصيل” — H. Download / preview.
- **button** “طباعة الموافقة” — G. Export.
- **button** “التفاصيل” — H. Download / preview.
- **button** “استعراض المرفق” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `employee/support.html`

- **a** “الرئيسية” — A. Native navigation.
- **a** “الطلبات الإدارية” — A. Native navigation.
- **a** “الخدمات المالية” — A. Native navigation.
- **a** “الدعم الفني والخدمات” — A. Native navigation.
- **a** “ملفاتي السحابية” — A. Native navigation.
- **a** “الاعتمادات والتواقيع 2” — A. Native navigation.
- **a** “الأداء والتدريب” — A. Native navigation.
- **a** “اللوائح والسياسات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “م. أيمن المغربي مهندس برمجيات” — A. Native navigation.
- **button** “محادثة حية (Live Chat)” — I. Communication.
- **button** “إنشاء تذكرة جديدة” — C. Create (business schema).
- **input** “البحث برقم التذكرة أو الموضوع...” — F. Current-page search/filter.
- **select** “جميع التصنيفات مشاكل أجهزة (Hardware) مشاكل برامج (Software) الشبكة والإنترنت (Network) صلاحيات وحسابات (Access)” — F. Native selection / table filter.
- **select** “جميع الحالات مفتوحة (Open) قيد العمل (In Progress) تم الحل (Resolved)” — F. Native selection / table filter.
- **button** “إضافة تعليق” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “التفاصيل” — H. Download / preview.
- **button** “إضافة تعليق” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “التفاصيل” — H. Download / preview.
- **button** “تقييم” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `finance/ap_bills.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **button** “إضافة فاتورة مورد” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “البحث برقم الفاتورة، اسم المورد...” — F. Current-page search/filter.
- **select** “جميع الموردين شركة أمازون (AWS) شركة الاتصالات (STC) مكتب العبيكان أخرى...” — F. Native selection / table filter.
- **select** “حالة الدفع مفتوحة (Open) متأخرة (Overdue) مسددة جزئياً (Partial) مسددة بالكامل (Paid)” — F. Native selection / table filter.
- **button** “عرض” — H. Download / preview.
- **button** “تسجيل دفعة” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “عرض السند” — H. Download / preview.
- **button** “تسجيل دفعة” — K. Backend-dependent (explicit explanation; no fake completion).

### `finance/ap_payments.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **button** “كشف المدفوعات” — H. Download / preview.
- **button** “إنشاء سند صرف جديد” — C. Create (business schema).
- **input** “البحث برقم السند، المورد، أو رقم الشيك...” — F. Current-page search/filter.
- **select** “طريقة الدفع حوالة بنكية شيك مصدق / عادي صندوق (نقدي)” — F. Native selection / table filter.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **button** “طباعة السند” — G. Export.
- **button** “إدارة الشيك” — D. Edit.
- **button** “عرض السند” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `finance/ap_vendors.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **button** “تصدير (Excel)” — G. Export.
- **button** “إضافة مورد جديد” — C. Create (business schema).
- **input** “البحث باسم المورد، الرقم الضريبي، أو رقم الاتصال...” — F. Current-page search/filter.
- **select** “جميع الحالات نشط غير نشط موقوف / تحت التقييم” — F. Native selection / table filter.
- **button** “كشف حساب” — H. Download / preview.
- **button** “تعديل البيانات” — D. Edit.
- **button** “كشف حساب” — H. Download / preview.
- **button** “تعديل البيانات” — D. Edit.
- **button** “كشف حساب” — H. Download / preview.
- **button** “تعديل البيانات” — D. Edit.
- **button** “كشف حساب” — H. Download / preview.
- **button** “تعديل البيانات” — D. Edit.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `finance/approvals.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات 4” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **button** “الكل” — F. Filter.
- **button** “الرواتب والأجور (HR)” — F. Filter.
- **button** “أوامر الشراء (PO)” — F. Filter.
- **button** “فواتير الموردين (AP)” — F. Filter.
- **button** “عهد ومصروفات (Expenses)” — F. Filter.
- **button** “اعتماد (توجيه للصرف)” — E. Workflow action.
- **button** “رفض / إرجاع” — E. Workflow action.
- **button** “عرض التفاصيل والمرفقات” — H. Download / preview.
- **button** “اعتماد (توجيه للصرف)” — E. Workflow action.
- **button** “رفض / إرجاع” — E. Workflow action.
- **button** “عرض التفاصيل والمرفقات” — H. Download / preview.
- **button** “اعتماد (توجيه للصرف)” — E. Workflow action.
- **button** “رفض / إرجاع” — E. Workflow action.
- **button** “عرض التفاصيل والمرفقات” — H. Download / preview.
- **button** “اعتماد (توجيه للصرف)” — E. Workflow action.
- **button** “رفض / إرجاع” — E. Workflow action.
- **button** “عرض التفاصيل والمرفقات” — H. Download / preview.

### `finance/ar_invoices.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **button** “كشف الذمم المدينة” — H. Download / preview.
- **button** “إصدار فاتورة جديدة” — C. Create (business schema).
- **input** “البحث برقم الفاتورة، اسم العميل، أو المشروع...” — F. Current-page search/filter.
- **select** “جميع العملاء عملاء القطاع الحكومي (GIC) عملاء الشركات (B2B) عملاء التجزئة (Retail)” — F. Native selection / table filter.
- **select** “حالة التحصيل غير مسددة (Unpaid) متأخرة (Overdue) مسددة بالكامل (Paid) مسودة (Draft)” — F. Native selection / table filter.
- **button** “عرض السند” — H. Download / preview.
- **button** “طباعة” — G. Export.
- **button** “تسجيل دفعة” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “إرسال تذكير” — E. Workflow action.
- **button** “تسجيل دفعة” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “إرسال تذكير” — E. Workflow action.
- **button** “تعديل واعتماد” — E. Workflow action.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `finance/ar_receipts.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **button** “تصدير الكشف” — G. Export.
- **button** “إنشاء سند قبض” — C. Create (business schema).
- **input** “البحث برقم السند، اسم العميل، أو رقم الشيك/الحوالة...” — F. Current-page search/filter.
- **select** “طريقة القبض حوالة بنكية شيك نقدي / نقاط بيع (POS)” — F. Native selection / table filter.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **button** “طباعة السند” — G. Export.
- **button** “إدارة الشيك” — D. Edit.
- **button** “طباعة السند” — G. Export.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `finance/fin_settings.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **button** “حفظ التغييرات” — J. Settings.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **button** “[icon]” — H. Download / preview.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **button** “[icon]” — H. Download / preview.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **select** “الريال السعودي (SAR) الدولار الأمريكي (USD)” — F. Native selection / table filter.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **input** “لا يمكن إدخال حركات قبل هذا التاريخ لجميع المستخدمين.” — Form field; page-specific form submission or backend integration.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **input** “SAR” — Form field; page-specific form submission or backend integration.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.

### `finance/gl_coa.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **button** “طباعة الدليل” — G. Export.
- **button** “إضافة حساب فرعي جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “البحث برقم الحساب أو اسم الحساب...” — F. Current-page search/filter.
- **select** “جميع أنواع الحسابات الأصول (Assets) الخصوم (Liabilities) حقوق الملكية (Equity) الإيرادات (Revenues) المصروفات (Expenses)” — F. Native selection / table filter.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “تعديل” — D. Edit.
- **button** “كشف حساب” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “تعديل” — D. Edit.
- **button** “كشف حساب” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `finance/gl_cost_centers.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **button** “تصدير (Excel)” — G. Export.
- **button** “إضافة مركز تكلفة” — C. Create (business schema).
- **input** “البحث برقم المركز، الاسم، أو القسم...” — F. Current-page search/filter.
- **select** “جميع الفئات الإدارات والأقسام الفروع الجغرافية المشاريع المستقلة” — F. Native selection / table filter.
- **button** “كشف حساب المركز” — H. Download / preview.
- **button** “كشف حساب المركز” — H. Download / preview.
- **button** “كشف حساب المركز” — H. Download / preview.
- **button** “كشف حساب المركز” — H. Download / preview.
- **button** “كشف حساب المركز” — H. Download / preview.

### `finance/gl_journal.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **button** “تصدير (Excel)” — G. Export.
- **button** “إنشاء قيد يومية” — C. Create (business schema).
- **input** “البحث برقم القيد أو البيان...” — F. Current-page search/filter.
- **select** “جميع الحالات مرحل (Posted) مسودة (Draft) بانتظار الاعتماد” — F. Native selection / table filter.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **button** “تفاصيل / ترحيل” — H. Download / preview.
- **button** “[icon]” — H. Download / preview.
- **button** “[icon]” — H. Download / preview.
- **button** “[icon]” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `finance/index.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **a** “قيد يومية جديد” — A. Native navigation.
- **a** “عرض الكل” — A. Native navigation.
- **button** “مراجعة” — E. Workflow action.
- **button** “مراجعة” — E. Workflow action.
- **button** “مراجعة” — E. Workflow action.
- **a** “إصدار فاتورة مبيعات B2B” — A. Native navigation.
- **a** “تسجيل دفعة مورد” — A. Native navigation.
- **a** “استعراض ميزان المراجعة” — A. Native navigation.

### `finance/internal_chat.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **input** “ابحث عن إدارة أو موظف...” — F. Current-page search/filter.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **textarea** “اكتب رسالتك هنا...” — Form field; page-specific form submission or backend integration.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `finance/inv_assets.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **button** “تشغيل الإهلاك الشهري” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “إضافة أصل جديد” — C. Create (business schema).
- **input** “البحث برمز الأصل، اسم الأصل، أو مركز التكلفة...” — F. Current-page search/filter.
- **select** “جميع فئات الأصول أجهزة حاسب وشبكات أثاث وتركيبات مكتبية سيارات ومركبات تراخيص وبرمجيات (أصول غير ملموسة)” — F. Native selection / table filter.
- **select** “حالة الأصل نشط (يُهلك) مهلك بالكامل مستبعد / مباع تحت الصيانة” — F. Native selection / table filter.
- **button** “سجل الإهلاك” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “تعديل” — D. Edit.
- **button** “سجل الإهلاك” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “تعديل” — D. Edit.
- **button** “سجل الإهلاك” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “استبعاد / بيع” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `finance/inv_dashboard.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **button** “جرد المخزون” — H. Download / preview.
- **button** “حركة مستودعية جديدة” — C. Create (business schema).
- **input** “البحث باسم الصنف، الباركود، أو رقم الحركة...” — F. Current-page search/filter.
- **select** “جميع المستودعات المستودع الرئيسي - الرياض مستودع الأجهزة - جدة مستودع التوالف” — F. Native selection / table filter.

### `finance/profile.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.

### `finance/rep_budget.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **button** “تصدير التقرير” — G. Export.
- **button** “تخصيص موازنة جديدة” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “بحث بالقسم، البند المالي...” — F. Current-page search/filter.
- **select** “العام المالي 2026 العام المالي 2025” — F. Native selection / table filter.
- **select** “كل الإدارات قطاع المبيعات القطاع التقني الموارد البشرية” — F. Native selection / table filter.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `finance/rep_statements.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **button** “طباعة” — G. Export.
- **button** “تصدير PDF” — G. Export.
- **button** “تصدير Excel” — G. Export.
- **button** “قائمة الدخل” — H. Download / preview.
- **button** “المركز المالي (الميزانية)” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “ميزان المراجعة” — E. Workflow action.
- **button** “التدفقات النقدية” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **select** “المؤسسة ككل (الرئيسي) قطاع المبيعات قطاع التقنية” — F. Native selection / table filter.
- **select** “المستوى 1 (رئيسي) المستوى 2 المستوى 3 مفصل (كل المستويات)” — F. Native selection / table filter.
- **button** “تحديث التقرير” — K. Backend-dependent (explicit explanation; no fake completion).

### `finance/rep_tax.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات” — A. Native navigation.
- **a** “المحادثات” — A. Native navigation.
- **a** “قيود اليومية” — A. Native navigation.
- **a** “دليل الحسابات” — A. Native navigation.
- **a** “مراكز التكلفة” — A. Native navigation.
- **a** “فواتير الموردين” — A. Native navigation.
- **a** “المدفوعات” — A. Native navigation.
- **a** “سجل الموردين” — A. Native navigation.
- **a** “فواتير العملاء” — A. Native navigation.
- **a** “المقبوضات” — A. Native navigation.
- **a** “لوحة المخزون” — A. Native navigation.
- **a** “الأصول الثابتة” — A. Native navigation.
- **a** “القوائم المالية” — A. Native navigation.
- **a** “الموازنات التقديرية” — A. Native navigation.
- **a** “الإقرارات الضريبية” — A. Native navigation.
- **a** “الإعدادات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “الإدارة المالية CFO / Chief Accountant” — A. Native navigation.
- **button** “تقرير المراجعة” — H. Download / preview.
- **button** “تجهيز إقرار ضريبي جديد” — E. Workflow action.
- **select** “العام المالي 2026 العام المالي 2025 العام المالي 2024” — F. Native selection / table filter.
- **select** “نوع الإقرار ضريبة القيمة المضافة (VAT) إقرار زكوي / ضريبة دخل ضريبة الاستقطاع” — F. Native selection / table filter.
- **button** “اعتماد للإرسال” — E. Workflow action.
- **button** “عرض الإيصال” — H. Download / preview.
- **button** “عرض الإيصال” — H. Download / preview.
- **button** “الشهادة الزكوية” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “عرض الإيصال” — H. Download / preview.

### `hr/hr_approvals.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **button** “الكل” — F. Filter.
- **button** “الإجازات والمغادرات” — F. Filter.
- **button** “خطابات التعريف” — F. Filter.
- **button** “السلف والعهد” — F. Filter.
- **button** “الرحلات والانتدابات” — F. Filter.
- **button** “اعتماد نهائي” — E. Workflow action.
- **button** “رفض” — E. Workflow action.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “إصدار واعتماد” — H. Download / preview.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “اعتماد وتحويل للمالية” — E. Workflow action.
- **button** “رفض” — E. Workflow action.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “اعتماد التذاكر والمصروفات” — E. Workflow action.
- **button** “رفض” — E. Workflow action.
- **button** “عرض التفاصيل والمرفقات” — H. Download / preview.

### `hr/hr_assets.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **button** “تصدير السجل” — G. Export.
- **button** “تسليم عهدة جديدة” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “البحث باسم الموظف، رقم العهدة، السيريال نمبر...” — F. Current-page search/filter.
- **select** “جميع التصنيفات أجهزة تقنية (IT) سيارات (Vehicles) بطاقات ومفاتيح (Access) خطوط اتصال (SIM)” — F. Native selection / table filter.
- **select** “حالة العهدة في حوزة الموظف مسترجعة مفقودة / تالفة” — F. Native selection / table filter.
- **button** “نموذج الاستلام” — H. Download / preview.
- **button** “تسجيل استرجاع” — E. Workflow action.
- **button** “نموذج الاستلام” — H. Download / preview.
- **button** “تسجيل استرجاع” — E. Workflow action.
- **button** “إلغاء التفعيل” — E. Workflow action.
- **button** “إصدار بدل فاقد” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “نموذج الاسترجاع / إخلاء الطرف” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `hr/hr_attendance.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **button** “تصدير (Excel)” — G. Export.
- **button** “سحب حركات البصمة” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “البحث برقم الموظف، الاسم...” — F. Current-page search/filter.
- **input** “جميع الإدارات الإدارة العامة تقنية المعلومات المبيعات والتسويق العمليات والتشغيل جميع الحالات حاضر (منتظم) متأخر غياب مغ” — Form field; page-specific form submission or backend integration.
- **select** “جميع الإدارات الإدارة العامة تقنية المعلومات المبيعات والتسويق العمليات والتشغيل” — F. Native selection / table filter.
- **select** “جميع الحالات حاضر (منتظم) متأخر غياب مغادرة مبكرة” — F. Native selection / table filter.
- **button** “تعديل يدوي” — D. Edit.
- **button** “تعديل يدوي / إضافة عذر” — D. Edit.
- **button** “عرض تفاصيل الإجازة” — H. Download / preview.
- **button** “تعديل الحالة” — D. Edit.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `hr/hr_contracts.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **button** “تصدير (Excel)” — G. Export.
- **button** “إنشاء عقد جديد” — C. Create (business schema).
- **input** “البحث برقم العقد، اسم الموظف...” — F. Current-page search/filter.
- **select** “جميع أنواع العقود عقد محدد المدة عقد غير محدد المدة عقد عمل مرن / عن بعد” — F. Native selection / table filter.
- **select** “حالة العقد ساري المفعول فترة التجربة قارب على الانتهاء منتهي / مفسوخ” — F. Native selection / table filter.
- **button** “عرض العقد” — H. Download / preview.
- **button** “تعديل” — D. Edit.
- **button** “تجديد العقد” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “إشعار بعدم التجديد” — J. Settings.
- **button** “عرض العقد” — H. Download / preview.
- **button** “تعديل” — D. Edit.
- **button** “مخالصة نهائية” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `hr/hr_employees.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **button** “تصدير (Excel)” — G. Export.
- **button** “إضافة موظف” — C. Create (business schema).
- **input** “البحث بالاسم، الرقم الوظيفي، أو المسمى...” — F. Current-page search/filter.
- **select** “جميع الإدارات الإدارة العامة تقنية المعلومات المبيعات والتسويق العمليات والتشغيل” — F. Native selection / table filter.
- **select** “حالة الموظف على رأس العمل في إجازة فترة التجربة مستقيل / منتهية خدماته” — F. Native selection / table filter.
- **button** “الملف الشخصي” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “تعديل” — D. Edit.
- **button** “الملف الشخصي” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “تعديل” — D. Edit.
- **button** “الملف الشخصي” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “تعديل” — D. Edit.
- **button** “السجل التاريخي” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `hr/hr_govt.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **button** “مزامنة البيانات” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “الدخول للمنصات” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “البحث بالاسم، رقم الإقامة، رقم المعاملة...” — F. Current-page search/filter.
- **select** “جميع المنصات منصة قوى (Qiwa) منصة مقيم (Muqeem) التأمينات (GOSI) منصة مُدد (Mudad)” — F. Native selection / table filter.
- **select** “جميع الحالات تتطلب إجراء قيد المعالجة مكتمل” — F. Native selection / table filter.
- **button** “إرسال طلب للمالية” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “إرسال تذكير للموظف” — A. Navigation / shared shell.
- **button** “عرض السجل” — H. Download / preview.
- **button** “طباعة الشهادة” — G. Export.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `hr/hr_leaves.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **button** “تقرير الأرصدة” — H. Download / preview.
- **button** “تسجيل إجازة يدوياً” — C. Create (business schema).
- **input** “البحث باسم الموظف أو رقم الطلب...” — F. Current-page search/filter.
- **select** “جميع الأنواع إجازة سنوية إجازة مرضية إجازة بدون راتب مغادرة قصيرة (إذن)” — F. Native selection / table filter.
- **select** “جميع الحالات بانتظار الاعتماد معتمد (ساري) مرفوض” — F. Native selection / table filter.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “اعتماد” — E. Workflow action.
- **button** “رفض” — E. Workflow action.
- **button** “المرفق (التقرير الطبي)” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “عرض التفاصيل والسبب” — H. Download / preview.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `hr/hr_logistics.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **button** “تقرير دوري” — H. Download / preview.
- **button** “طلب خدمة جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “البحث برقم الطلب، القسم، أو التفاصيل...” — F. Current-page search/filter.
- **select** “جميع أنواع الخدمات صيانة (تكييف، كهرباء...) أثاث ومكاتب أدوات مكتبية وقرطاسية نقل ومراسلات” — F. Native selection / table filter.
- **select** “جميع الحالات بانتظار الاعتماد قيد المعالجة والتنفيذ مكتمل” — F. Native selection / table filter.
- **button** “إغلاق الطلب” — E. Workflow action.
- **button** “التفاصيل” — H. Download / preview.
- **button** “التفاصيل” — H. Download / preview.
- **button** “تأكيد الاستلام” — E. Workflow action.
- **button** “التفاصيل” — H. Download / preview.
- **button** “التفاصيل” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `hr/hr_org.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **button** “تصدير الهيكل” — G. Export.
- **button** “إضافة قسم جديد” — C. Create (business schema).
- **button** “طي الكل” — F. Filter.
- **button** “[icon]” — D. Edit.

### `hr/hr_partners.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **button** “تصدير البيانات” — G. Export.
- **button** “إضافة شريك جديد” — C. Create (business schema).
- **input** “البحث باسم الشريك، رقم العقد، مسؤول التواصل...” — F. Current-page search/filter.
- **select** “جميع التصنيفات تأمين طبي / حياة وكالات توظيف مراكز تدريب وتطوير استشارات موارد بشرية” — F. Native selection / table filter.
- **select** “جميع الحالات ساري المفعول قيد التجديد منتهي” — F. Native selection / table filter.
- **button** “بوابة الشريك (الشبكة الطبية)” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “إدارة المطالبات” — H. Download / preview.
- **button** “عرض العقد والتفاصيل” — H. Download / preview.
- **button** “تجديد العقد” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “عرض العقد” — H. Download / preview.
- **button** “سجل الوثائق” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `hr/hr_payroll.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **button** “تصدير WPS للبنك” — G. Export.
- **button** “إنشاء مسير الشهر الحالي” — K. Backend-dependent (explicit explanation; no fake completion).
- **select** “العام المالي 2026 العام المالي 2025” — F. Native selection / table filter.
- **select** “جميع الحالات مسودة (Draft) معتمد HR مصروف (Paid)” — F. Native selection / table filter.
- **button** “عرض التفاصيل والموظفين” — H. Download / preview.
- **button** “إرسال للمالية” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “سندات الصرف” — H. Download / preview.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “سندات الصرف” — H. Download / preview.

### `hr/hr_purchases.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **button** “تقرير المصروفات” — H. Download / preview.
- **button** “طلب شراء جديد (PR)” — C. Create (business schema).
- **input** “البحث برقم الطلب (PR)، الوصف، أو القسم...” — F. Current-page search/filter.
- **select** “جميع التصنيفات أدوات قرطاسية ومكتبية ضيافة ومأكولات أدوات نظافة أثاث ومعدات صغيرة” — F. Native selection / table filter.
- **select** “جميع الحالات بانتظار اعتماد الموارد محول للمشتريات/المالية تم الشراء (مكتمل)” — F. Native selection / table filter.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “متابعة مع المشتريات” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “الفاتورة (PO)” — H. Download / preview.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “عرض التفاصيل” — H. Download / preview.
- **button** “الفاتورة (PO)” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `hr/hr_recruitment.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **button** “لوحة الوظائف” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “نشر وظيفة جديدة” — C. Create (business schema).
- **input** “البحث باسم المتقدم، التخصص...” — F. Current-page search/filter.
- **select** “تصفية حسب الوظيفة مطور واجهات أمامية (Front-End) أخصائي تسويق رقمي محاسب مالي مهندس شبكات” — F. Native selection / table filter.
- **select** “حالة الطلب جديد (قيد المراجعة) مقابلة فنية مجدولة مرحلة العرض الوظيفي مرفوض / غير مناسب” — F. Native selection / table filter.
- **button** “عرض السيرة الذاتية” — H. Download / preview.
- **button** “إدارة المقابلة” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “عرض السيرة الذاتية” — H. Download / preview.
- **button** “ترشيح للمقابلة” — E. Workflow action.
- **button** “رفض” — E. Workflow action.
- **button** “متابعة العرض” — H. Download / preview.
- **button** “عرض التقييم” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `hr/hr_trips.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **button** “تقرير المصروفات” — H. Download / preview.
- **button** “تسجيل انتداب جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “البحث برقم الطلب، اسم الموظف، الوجهة...” — F. Current-page search/filter.
- **select** “جميع الوجهات داخل المملكة (محلي) خارج المملكة (دولي)” — F. Native selection / table filter.
- **select** “جميع الحالات بانتظار الاعتماد مهمة جارية مكتمل ملغى / مرفوض” — F. Native selection / table filter.
- **button** “اعتماد وتحويل للوكالة” — E. Workflow action.
- **button** “التفاصيل” — H. Download / preview.
- **button** “التذاكر والمرفقات” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “التفاصيل” — H. Download / preview.
- **button** “سند تسوية العهدة” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `hr/index.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **a** “إضافة موظف جديد” — A. Native navigation.
- **a** “عرض الكل” — A. Native navigation.
- **button** “مراجعة” — E. Workflow action.
- **button** “مراجعة” — E. Workflow action.
- **button** “مراجعة” — E. Workflow action.
- **a** “بدء إجراءات التجديد” — K. Placeholder link; backend or route configuration required.
- **a** “طلب تقييم المدراء” — K. Placeholder link; backend or route configuration required.
- **a** “عرض المرشحين (24)” — A. Native navigation.

### `hr/internal_chat.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.
- **input** “البحث عن موظف، إدارة، قسم...” — F. Current-page search/filter.
- **button** “الكل” — F. Filter.
- **button** “الإدارات” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “الاستفسارات” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — I. Communication.
- **button** “[icon]” — I. Communication.
- **button** “[icon]” — B. Modal / drawer.
- **button** “[icon]” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **textarea** “اكتب رسالتك للإدارة المالية...” — Form field; page-specific form submission or backend integration.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `hr/profile.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “الاعتمادات والطلبات 15” — A. Native navigation.
- **a** “المحادثات الداخلية” — A. Native navigation.
- **a** “دليل الموظفين” — A. Native navigation.
- **a** “العقود الوظيفية” — A. Native navigation.
- **a** “الهيكل التنظيمي” — A. Native navigation.
- **a** “الحضور والانصراف” — A. Native navigation.
- **a** “الإجازات والمغادرات” — A. Native navigation.
- **a** “مسيرات الرواتب” — A. Native navigation.
- **a** “رحلات العمل والانتدابات” — A. Native navigation.
- **a** “عهد الموظفين” — A. Native navigation.
- **a** “الخدمات اللوجستية” — A. Native navigation.
- **a** “مشتريات الإدارة” — A. Native navigation.
- **a** “شركاء التوظيف والتأمين” — A. Native navigation.
- **a** “الخدمات الحكومية” — A. Native navigation.
- **a** “التوظيف والمقابلات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة الموارد البشرية HR Manager” — A. Native navigation.

### `index.html`

- **button** “[icon]” — A. Navigation / shared shell.
- **a** “تسجيل الخروج” — A. Native navigation.
- **a** “الإدارة العليا (CEO) مركز اتخاذ القرار، لوحات المؤشرات الاستراتيجية، ومتابعة الأداء العام للشركة. الدخول للبوابة” — A. Native navigation.
- **a** “الإدارة المالية (CFO) إدارة الحسابات، التدفقات النقدية، الميزانيات، الرواتب، والمصاريف التشغيلية. الدخول للبوابة” — A. Native navigation.
- **a** “الموارد البشرية (HR) إدارة شؤون الموظفين، الحضور والانصراف، التوظيف، وتقييم الأداء السنوي. الدخول للبوابة” — A. Native navigation.
- **a** “المبيعات والتسويق إدارة علاقات العملاء (CRM)، الفرص البيعية (Pipeline)، عروض الأسعار والمستهدفات. الدخول للبوابة” — A. Native navigation.
- **a** “تقنية المعلومات (IT) إدارة البنية التحتية، الخوادم، الأمن السيبراني (SOC)، نظام السنترال والدعم الفني. الدخول للبوابة” — A. Native navigation.
- **a** “المراجعة والتدقيق مراقبة الامتثال، تدقيق العمليات المالية والإدارية، تقييم المخاطر والحوكمة المكتسبة. الدخول للبوابة” — A. Native navigation.
- **a** “مساحة الموظف (الخدمة الذاتية) مساحتك الرقمية المتكاملة.. لتقديم الطلبات الإدارية، استعراض مسيرات الرواتب، رفع ملفاتك الس” — A. Native navigation.

### `login.html`

- **button** “العودة للرئيسية” — B. Modal / drawer.
- **button** “تبديل المظهر” — A. Navigation / shared shell.
- **input** “أدخل اسم المستخدم” — Form field; page-specific form submission or backend integration.
- **input** “أدخل كلمة المرور” — Form field; page-specific form submission or backend integration.
- **a** “نسيت كلمة المرور؟” — K. Placeholder link; backend or route configuration required.
- **button** “دخول النظام” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “الإدارة العليا / المشرف المشرف العام” — A. Navigation.
- **button** “مجلس الإدارة أ. عبد الله الحواس” — A. Navigation.
- **button** “الرئيس التنفيذي أ. هيثم السحيباني” — A. Navigation.
- **button** “بوابة المساهمين سجل إيداع (تداول)” — A. Navigation.
- **button** “الإدارة المالية القوائم والموازنة” — A. Navigation.
- **button** “الموارد البشرية شؤون الموظفين” — A. Navigation.
- **button** “المراجعة الداخلية تقارير الضبط” — A. Navigation.
- **button** “العمليات التقنية تطوير النظم والتشغيل” — A. Navigation.
- **button** “قطاع المبيعات إدارة الحسابات” — A. Navigation.
- **button** “بوابة الموظف الخدمات الذاتية” — A. Navigation.

### `sales/index.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “فرص البيع (Pipeline)” — A. Native navigation.
- **a** “عروض الأسعار” — A. Native navigation.
- **a** “العقود والاتفاقيات” — A. Native navigation.
- **a** “دليل العملاء (CRM)” — A. Native navigation.
- **a** “الأنشطة والاجتماعات 3” — A. Native navigation.
- **a** “المستهدفات والعمولات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة المبيعات Sales Director” — A. Native navigation.
- **a** “عرض سعر جديد” — A. Native navigation.
- **a** “عرض الكل” — A. Native navigation.
- **a** “الجدول الكامل” — A. Native navigation.

### `sales/profile.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “فرص البيع (Pipeline)” — A. Native navigation.
- **a** “عروض الأسعار” — A. Native navigation.
- **a** “العقود والاتفاقيات” — A. Native navigation.
- **a** “دليل العملاء (CRM)” — A. Native navigation.
- **a** “الأنشطة والاجتماعات 3” — A. Native navigation.
- **a** “المستهدفات والعمولات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة المبيعات Sales Director” — A. Native navigation.

### `sales/sales_activities.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “فرص البيع (Pipeline)” — A. Native navigation.
- **a** “عروض الأسعار” — A. Native navigation.
- **a** “العقود والاتفاقيات” — A. Native navigation.
- **a** “دليل العملاء (CRM)” — A. Native navigation.
- **a** “الأنشطة والاجتماعات 3” — A. Native navigation.
- **a** “المستهدفات والعمولات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة المبيعات Sales Director” — A. Native navigation.
- **button** “مزامنة مع Outlook” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “إضافة نشاط” — C. Create (business schema).
- **input** “البحث بوصف المهمة، العميل، أو المندوب...” — F. Current-page search/filter.
- **input** “جميع أنواع الأنشطة مكالمة (Call) اجتماع (Meeting) عرض نظام (Demo) بريد إلكتروني (Email) حالة النشاط مجدول (Scheduled) قي” — Form field; page-specific form submission or backend integration.
- **select** “جميع أنواع الأنشطة مكالمة (Call) اجتماع (Meeting) عرض نظام (Demo) بريد إلكتروني (Email)” — F. Native selection / table filter.
- **select** “حالة النشاط مجدول (Scheduled) قيد الانتظار (Pending) مكتمل (Completed) متأخر (Overdue)” — F. Native selection / table filter.
- **button** “تحديد كمكتمل” — E. Workflow action.
- **button** “تعديل” — D. Edit.
- **button** “تحديد كمكتمل” — E. Workflow action.
- **button** “تعديل” — D. Edit.
- **button** “تحديد كمكتمل” — E. Workflow action.
- **button** “تعديل” — D. Edit.
- **button** “تحديد كمكتمل” — E. Workflow action.
- **button** “إعادة جدولة” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “التفاصيل” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `sales/sales_clients.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “فرص البيع (Pipeline)” — A. Native navigation.
- **a** “عروض الأسعار” — A. Native navigation.
- **a** “العقود والاتفاقيات” — A. Native navigation.
- **a** “دليل العملاء (CRM)” — A. Native navigation.
- **a** “الأنشطة والاجتماعات 3” — A. Native navigation.
- **a** “المستهدفات والعمولات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة المبيعات Sales Director” — A. Native navigation.
- **button** “استيراد / تصدير” — G. Export.
- **button** “إضافة جهة (عميل)” — C. Create (business schema).
- **input** “البحث باسم الجهة، السجل التجاري (CR)، رقم الهاتف...” — F. Current-page search/filter.
- **select** “جميع القطاعات القطاع الحكومي (B2G) القطاع الخاص (B2B) القطاع التعليمي القطاع الصحي” — F. Native selection / table filter.
- **select** “حالة العميل عميل حالي / نشط عميل محتمل (Lead) عميل سابق (Inactive)” — F. Native selection / table filter.
- **button** “ملف العميل” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “إضافة نشاط / اجتماع” — C. Create (business schema).
- **button** “ملف العميل” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “إضافة نشاط / اجتماع” — C. Create (business schema).
- **button** “ملف العميل” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “إضافة نشاط / اجتماع” — C. Create (business schema).
- **button** “ملف العميل” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `sales/sales_contracts.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “فرص البيع (Pipeline)” — A. Native navigation.
- **a** “عروض الأسعار” — A. Native navigation.
- **a** “العقود والاتفاقيات” — A. Native navigation.
- **a** “دليل العملاء (CRM)” — A. Native navigation.
- **a** “الأنشطة والاجتماعات 3” — A. Native navigation.
- **a** “المستهدفات والعمولات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة المبيعات Sales Director” — A. Native navigation.
- **button** “تصدير سجل العقود” — G. Export.
- **button** “تسجيل عقد جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “البحث برقم العقد، اسم العميل، أو نوع الخدمة...” — F. Current-page search/filter.
- **select** “جميع أنواع العقود عقد تراخيص أنظمة (Licenses) عقد دعم وصيانة (SLA) عقد تطوير مخصص” — F. Native selection / table filter.
- **select** “حالة العقد سارٍ (Active) ينتهي قريباً (Expiring Soon) بانتظار التوقيع منتهي (Expired)” — F. Native selection / table filter.
- **button** “استعراض العقد PDF” — G. Export.
- **button** “بدء تجديد العقد” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “استعراض العقد PDF” — G. Export.
- **button** “إرسال للتوقيع الإلكتروني” — D. Edit.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `sales/sales_pipeline.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “فرص البيع (Pipeline)” — A. Native navigation.
- **a** “عروض الأسعار” — A. Native navigation.
- **a** “العقود والاتفاقيات” — A. Native navigation.
- **a** “دليل العملاء (CRM)” — A. Native navigation.
- **a** “الأنشطة والاجتماعات 3” — A. Native navigation.
- **a** “المستهدفات والعمولات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة المبيعات Sales Director” — A. Native navigation.
- **button** “عرض قائمة” — H. Download / preview.
- **button** “إضافة فرصة جديدة” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “البحث برقم الصفقة، اسم العميل، أو المندوب...” — F. Current-page search/filter.
- **select** “جميع المندوبين سعد العتيبي نورة القحطاني فهد الشمري” — F. Native selection / table filter.
- **select** “الربع الرابع (Q4 2026) الربع الثالث (Q3 2026)” — F. Native selection / table filter.

### `sales/sales_quotes.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “فرص البيع (Pipeline)” — A. Native navigation.
- **a** “عروض الأسعار” — A. Native navigation.
- **a** “العقود والاتفاقيات” — A. Native navigation.
- **a** “دليل العملاء (CRM)” — A. Native navigation.
- **a** “الأنشطة والاجتماعات 3” — A. Native navigation.
- **a** “المستهدفات والعمولات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة المبيعات Sales Director” — A. Native navigation.
- **button** “تصدير (PDF/Excel)” — G. Export.
- **button** “إنشـاء عرض سعر” — H. Download / preview.
- **input** “البحث برقم العرض، اسم العميل، أو المندوب...” — F. Current-page search/filter.
- **select** “جميع الحالات مسودة (Draft) مرسل للعميل (Sent) مقبول (Accepted) مرفوض (Rejected) منتهي الصلاحية (Expired)” — F. Native selection / table filter.
- **select** “جميع المندوبين سعد العتيبي نورة القحطاني فهد الشمري” — F. Native selection / table filter.
- **button** “عرض العرض (PDF)” — G. Export.
- **button** “تحويل لعقد” — H. Download / preview.
- **button** “عرض العرض (PDF)” — G. Export.
- **button** “إعادة إرسال تذكير” — E. Workflow action.
- **button** “تعديل العرض” — H. Download / preview.
- **button** “تجديد العرض” — H. Download / preview.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “1” — A. Navigation / pagination.
- **button** “2” — A. Navigation / pagination.
- **button** “3” — A. Navigation / pagination.
- **button** “[icon]” — K. Backend-dependent (explicit explanation; no fake completion).

### `sales/sales_targets.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “فرص البيع (Pipeline)” — A. Native navigation.
- **a** “عروض الأسعار” — A. Native navigation.
- **a** “العقود والاتفاقيات” — A. Native navigation.
- **a** “دليل العملاء (CRM)” — A. Native navigation.
- **a** “الأنشطة والاجتماعات 3” — A. Native navigation.
- **a** “المستهدفات والعمولات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “إدارة المبيعات Sales Director” — A. Native navigation.
- **button** “احتساب عمولات Q4” — K. Backend-dependent (explicit explanation; no fake completion).
- **button** “ضبط مستهدف جديد” — K. Backend-dependent (explicit explanation; no fake completion).
- **input** “البحث باسم المندوب، المسمى الوظيفي، أو المنطقة...” — F. Current-page search/filter.
- **select** “الفترة المالية السنة الكاملة 2026 الربع الرابع (Q4) الربع الثالث (Q3)” — F. Native selection / table filter.
- **select** “مستوى الإنجاز تجاوز المستهدف (>100%) في المسار الصحيح (80%-100%) يتطلب متابعة (<80%)” — F. Native selection / table filter.
- **button** “تفاصيل العمولات” — H. Download / preview.
- **button** “تفاصيل العمولات” — H. Download / preview.
- **button** “تفاصيل العمولات” — H. Download / preview.
- **button** “تفاصيل العمولات” — H. Download / preview.

### `shareholder/certificates.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “شهادات الأسهم” — A. Native navigation.
- **a** “توزيعات الأرباح” — A. Native navigation.
- **a** “التصويت الإلكتروني” — A. Native navigation.
- **a** “الطلبات والاستفسارات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “مساهم كريم محفظة إيداع مثرية” — A. Native navigation.
- **button** “طباعة شهادة جديدة” — G. Export.

### `shareholder/dividends.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “شهادات الأسهم” — A. Native navigation.
- **a** “توزيعات الأرباح” — A. Native navigation.
- **a** “التصويت الإلكتروني” — A. Native navigation.
- **a** “الطلبات والاستفسارات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “مساهم كريم محفظة إيداع مثرية” — A. Native navigation.
- **button** “تصدير الكشف (Excel)” — G. Export.

### `shareholder/index.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “شهادات الأسهم” — A. Native navigation.
- **a** “توزيعات الأرباح” — A. Native navigation.
- **a** “التصويت الإلكتروني” — A. Native navigation.
- **a** “الطلبات والاستفسارات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “مساهم كريم محفظة إيداع مثرية” — A. Native navigation.
- **a** “التصويت الإلكتروني المتاح” — A. Native navigation.
- **a** “الانتقال لشاشة التصويت” — A. Native navigation.
- **a** “شهادة ملكية الأسهم طباعة شهادة موثقة إلكترونياً” — A. Native navigation.
- **a** “إشعار الأرباح الموزعة كشف التحويلات والبنك المعتمد” — A. Native navigation.
- **a** “طلب استفسار لمجلس الإدارة تواصل مباشر مع أمانة سر المجلس” — A. Native navigation.

### `shareholder/profile.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “شهادات الأسهم” — A. Native navigation.
- **a** “توزيعات الأرباح” — A. Native navigation.
- **a** “التصويت الإلكتروني” — A. Native navigation.
- **a** “الطلبات والاستفسارات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “مساهم كريم محفظة إيداع مثرية” — A. Native navigation.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **input** “[icon]” — Form field; page-specific form submission or backend integration.
- **input** “••••••••” — Form field; page-specific form submission or backend integration.
- **input** “••••••••” — Form field; page-specific form submission or backend integration.
- **button** “تحديث كلمة المرور” — K. Backend-dependent (explicit explanation; no fake completion).

### `shareholder/requests.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “شهادات الأسهم” — A. Native navigation.
- **a** “توزيعات الأرباح” — A. Native navigation.
- **a** “التصويت الإلكتروني” — A. Native navigation.
- **a** “الطلبات والاستفسارات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “مساهم كريم محفظة إيداع مثرية” — A. Native navigation.
- **select** “استفسار عن توزيعات الأرباح تحديث الحساب البنكي / الآيبان استفسار موجه لمجلس الإدارة طلب وثائق وشهادات ملكية أخرى” — F. Native selection / table filter.
- **input** “مثال: استفسار حول تحويل أرباح 2026” — Form field; page-specific form submission or backend integration.
- **textarea** “اكتب تفاصيل طلبك بوضوح هنا...” — Form field; page-specific form submission or backend integration.
- **input** “[icon]” — K. File picker only; secure upload storage requires backend.
- **button** “إرسال الطلب” — K. Backend-dependent (explicit explanation; no fake completion).

### `shareholder/voting.html`

- **a** “نظرة عامة” — A. Native navigation.
- **a** “شهادات الأسهم” — A. Native navigation.
- **a** “توزيعات الأرباح” — A. Native navigation.
- **a** “التصويت الإلكتروني” — A. Native navigation.
- **a** “الطلبات والاستفسارات” — A. Native navigation.
- **a** “الملف الشخصي” — A. Native navigation.
- **a** “تسجيل الخروج” — A. Native navigation.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **button** “[icon]” — A. Navigation / shared shell.
- **a** “مساهم كريم محفظة إيداع مثرية” — A. Native navigation.
- **input** “موافق” — Form field; page-specific form submission or backend integration.
- **input** “غير موافق” — Form field; page-specific form submission or backend integration.
- **input** “امتناع” — Form field; page-specific form submission or backend integration.
- **input** “موافق” — Form field; page-specific form submission or backend integration.
- **input** “غير موافق” — Form field; page-specific form submission or backend integration.
- **input** “امتناع” — Form field; page-specific form submission or backend integration.
- **input** “موافق” — Form field; page-specific form submission or backend integration.
- **input** “غير موافق” — Form field; page-specific form submission or backend integration.
- **input** “امتناع” — Form field; page-specific form submission or backend integration.
- **button** “اعتماد وإرسال نتائج التصويت” — E. Workflow action.

