# ERPNext Real Estate

A Frappe/ERPNext app that installs a complete commercial real estate broker 
workflow, including custom fields, workspaces, and Kanban boards.

## What it installs

**Custom Fields — Item (Property)**
60+ fields covering property details: address, SqFt, cap rate, NOI, asking price,
sale price, lease terms, zoning, FEMA data, parking, building class, and more.
Properties are managed as Items in ERPNext.

**Custom Fields — Lead**
40+ fields for lead qualification across four transaction types:
- Buyer qualification (loan approval, brokerage agreement, deposit verification)
- Seller qualification (ownership, property condition, listing agreement)
- Tenant qualification (rental application, credit check, proof of income)
- Landlord qualification (ownership, property condition, brokerage agreement)

**Custom Fields — Customer (Client)**
30+ fields mirroring Lead qualification fields, populated on conversion.
Covers buyer, seller, tenant, and landlord profiles.

**Custom Fields — Opportunity**
20+ fields for RE transaction management:
- RE Sale Stage, RE Buy Stage, RE Lease Stage (Tenant/Landlord)
- Sales Partners 1-3 with type and commission fields
- Supplier Partners 1-3 with type fields
- Due diligence date

**Custom Fields — Contact**
- Source (Link)

**Workspace — Real Estate**
Single workspace with shortcuts to Properties, Leads, Opportunities (by type),
Clients, Partners, Contacts, and utility links for document imports.

**Kanban Boards**
- Lead Status Board — Lead pipeline by status
- RE Sales — Opportunity pipeline for sales
- RE Buys — Opportunity pipeline for acquisitions
- RE Leases (Landlord) — Landlord lease pipeline
- RE Leases (Tenant) — Tenant lease pipeline

**Setup ToDo Checklist**
On install, creates a guided setup checklist covering company config,
agent/partner setup, opportunity types, property import, and workflow testing.

## Transaction Flow

`Lead → Qualify (Buyer/Seller/Tenant/Landlord) → Convert to Customer → 
Opportunity (RE Sales/Buy/Lease) → Close → Invoice`

## Requirements

- ERPNext v15
- Properties managed as Items (Item Group: Properties recommended)

## Installation

Add to `apps.json` at Docker build time:
```json
{
    "url": "https://github.com/Mseethaler/erpnext_realestate",
    "branch": "main"
}
```

Then install on your site:
```bash
bench --site [your-site] install-app erpnext_realestate
```
