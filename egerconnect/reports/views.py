from django.shortcuts import render
from posts.models import SupportRequest
from django.utils import timezone
from datetime import timedelta, datetime
from collections import Counter
import calendar

from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime

from posts.models import Notice, Events, LostAndFound, Scholarship


User = get_user_model()

def support_requests_report(request):
    today = timezone.now()
    
    # Total requests
    total_requests = SupportRequest.objects.count()
    
    # ----- Weeks of Current Month -----
    start_of_month = today.replace(day=1)
    last_day = calendar.monthrange(today.year, today.month)[1]
    end_of_month = today.replace(day=last_day)

    week_counts = []
    week_labels = []
    start_week = start_of_month
    while start_week <= end_of_month:
        end_week = start_week + timedelta(days=6)
        if end_week > end_of_month:
            end_week = end_of_month
        count = SupportRequest.objects.filter(
            created_at__date__gte=start_week.date(),
            created_at__date__lte=end_week.date()
        ).count()
        week_counts.append(count)
        week_labels.append(f"{start_week.day}-{end_week.day}")
        start_week = end_week + timedelta(days=1)

    total_weeks = sum(week_counts)
    
    # ----- Months of Current Year -----
    monthly_counts = []
    month_labels = []
    for m in range(1, 13):
        start_month = datetime(today.year, m, 1)
        last_day = calendar.monthrange(today.year, m)[1]
        end_month = datetime(today.year, m, last_day)
        count = SupportRequest.objects.filter(
            created_at__date__gte=start_month.date(),
            created_at__date__lte=end_month.date()
        ).count()
        monthly_counts.append(count)
        month_labels.append(calendar.month_abbr[m])
    
    total_months = sum(monthly_counts)
    
    # ----- Requests by Year (last 5 years for example) -----
    years = range(today.year-4, today.year+1)
    yearly_counts = []
    year_labels = []
    for y in years:
        start_year = datetime(y, 1, 1)
        end_year = datetime(y, 12, 31)
        count = SupportRequest.objects.filter(
            created_at__date__gte=start_year.date(),
            created_at__date__lte=end_year.date()
        ).count()
        yearly_counts.append(count)
        year_labels.append(str(y))
    
    total_years = sum(yearly_counts)
    
    # Status breakdown
    pending_count = SupportRequest.objects.filter(status='pending').count()
    accepted_count = SupportRequest.objects.filter(status='accepted').count()
    declined_count = SupportRequest.objects.filter(status='declined').count()

    # Acceptance rate
    acceptance_rate = round((accepted_count / total_requests) * 100, 2) if total_requests > 0 else 0
    
    # Most common request types
    request_types = SupportRequest.objects.values_list('type_of_need', flat=True)
    most_common_types = Counter(request_types).most_common(5)
    
    context = {
        'total_requests': total_requests,
        'week_counts': week_counts,
        'week_labels': week_labels,
        'total_weeks': total_weeks,
        'monthly_counts': monthly_counts,
        'month_labels': month_labels,
        'total_months': total_months,
        'yearly_counts': yearly_counts,
        'year_labels': year_labels,
        'total_years': total_years,
        'pending_count': pending_count,
        'accepted_count': accepted_count,
        'declined_count': declined_count,
        'acceptance_rate': acceptance_rate,
        'most_common_types': most_common_types,
    }

    return render(request, 'reports/dashboard.html', context)  

def user_analysis_report(request):
    today = datetime.today() 
    current_year = today.year
    current_month_name = today.strftime("%B")

    context = {
        'current_year': current_year,
        'current_month_name': current_month_name,
    }
    
    
    
    today = timezone.now()

    # Total users
    total_users = User.objects.count()

    # ---- Users joined this month ----
    start_of_month = today.replace(day=1)
    users_joined = User.objects.filter(created_at__gte=start_of_month).count()

    # ---- Previous month ----
    if today.month == 1:
        prev_month_start = datetime(today.year - 1, 12, 1)
        prev_month_end = datetime(today.year - 1, 12, 31)
    else:
        prev_month_start = datetime(today.year, today.month - 1, 1)
        last_day_prev = (datetime(today.year, today.month, 1) - timedelta(days=1)).day
        prev_month_end = datetime(today.year, today.month - 1, last_day_prev)

    prev_month_users = User.objects.filter(
        created_at__gte=prev_month_start,
        created_at__lte=prev_month_end
    ).count()

    # ---- Monthly Growth ----
    if prev_month_users > 0:
        growth_percent = round(((users_joined - prev_month_users) / prev_month_users) * 100, 2)
    else:
        growth_percent = 0

    growth_diff = users_joined - prev_month_users

    if growth_diff > 0:
        growth_label = f"+{growth_percent}% ↑"
        growth_class = "positive"
    elif growth_diff < 0:
        growth_label = f"{growth_percent}% ↓"
        growth_class = "negative"
    else:
        growth_label = "0%"
        growth_class = "neutral"

    # ---- Weekly Users (current month) ----
    week_counts = []
    week_labels = []
    last_day = calendar.monthrange(today.year, today.month)[1]
    end_of_month = today.replace(day=last_day)
    start_week = start_of_month

    while start_week <= end_of_month:
        end_week = start_week + timedelta(days=6)
        if end_week > end_of_month:
            end_week = end_of_month

        count = User.objects.filter(
            created_at__date__gte=start_week.date(),
            created_at__date__lte=end_week.date()
        ).count()

        week_counts.append(count)
        week_labels.append(f"{start_week.day}-{end_week.day}")

        start_week = end_week + timedelta(days=1)

    # ---- Monthly Users (yearly graph) ----
    monthly_counts = []
    month_labels = []

    for m in range(1, 13):
        start_month = datetime(today.year, m, 1)
        last_day = calendar.monthrange(today.year, m)[1]
        end_month = datetime(today.year, m, last_day)

        count = User.objects.filter(
            created_at__gte=start_month,
            created_at__lte=end_month
        ).count()

        monthly_counts.append(count)
        month_labels.append(calendar.month_abbr[m])

    # ---- Yearly Users (last 5 years) ----
    years = range(today.year - 4, today.year + 1)
    year_labels = []
    year_counts = []

    for y in years:
        start_year = datetime(y, 1, 1)
        end_year = datetime(y, 12, 31)

        count = User.objects.filter(
            created_at__gte=start_year,
            created_at__lte=end_year
        ).count()

        year_labels.append(str(y))
        year_counts.append(count)

    # ---- Yearly Growth ----
    start_of_year = datetime(today.year, 1, 1)
    users_this_year = User.objects.filter(created_at__gte=start_of_year).count()

    prev_year_start = datetime(today.year - 1, 1, 1)
    prev_year_end = datetime(today.year - 1, 12, 31)
    prev_year_users = User.objects.filter(
        created_at__gte=prev_year_start,
        created_at__lte=prev_year_end
    ).count()

    yearly_diff = users_this_year - prev_year_users
    if prev_year_users > 0:
        yearly_growth_percent = round((yearly_diff / prev_year_users) * 100, 2)
    else:
        yearly_growth_percent = 0

    if yearly_diff > 0:
        yearly_growth_label = f"+{yearly_growth_percent}% ↑"
        yearly_growth_class = "positive"
    elif yearly_diff < 0:
        yearly_growth_label = f"{yearly_growth_percent}% ↓"
        yearly_growth_class = "negative"
    else:
        yearly_growth_label = "0%"
        yearly_growth_class = "neutral"

    # ---- Context ----
    context = {
    'total_users': total_users,
    'growth_label': growth_label,
    'growth_class': growth_class,
    'yearly_growth_label': yearly_growth_label,
    'yearly_growth_class': yearly_growth_class,

    # ✅ ADD THESE HERE (THIS IS THE FIX)
    'current_year': current_year,
    'current_month_name': current_month_name,

    'week_counts': week_counts,
    'week_labels': week_labels,
    'monthly_counts': monthly_counts,
    'month_labels': month_labels,
    'year_labels': year_labels,
    'year_counts': year_counts,
}

    return render(request, 'reports/user_dashboard.html', context)


def posts_report(request):
    today = timezone.now()

    # ----- Total Posts -----
    total_notices = Notice.objects.count()
    total_events = Events.objects.count()
    total_lost_found = LostAndFound.objects.count()
    total_scholarships = Scholarship.objects.count()
    total_posts = total_notices + total_events + total_lost_found + total_scholarships

    # ----- Posts by Category -----
    posts_by_category = {
        "Notices": total_notices,
        "Events": total_events,
        "Lost & Found": total_lost_found,
        "Scholarships": total_scholarships,
    }

    # Convert dict to lists for Chart.js
    category_labels = list(posts_by_category.keys())
    category_counts = list(posts_by_category.values())

    # ----- Most Used Category -----
    most_used_category = max(posts_by_category.items(), key=lambda x: x[1])[0] if total_posts > 0 else None

    # ----- Posts created this month -----
    start_of_month = today.replace(day=1)
    posts_this_month = (
        Notice.objects.filter(created_at__gte=start_of_month).count() +
        Events.objects.filter(created_at__gte=start_of_month).count() +
        LostAndFound.objects.filter(created_at__gte=start_of_month).count() +
        Scholarship.objects.filter(created_at__gte=start_of_month).count()
    )

    context = {
        "total_posts": total_posts,
        "posts_by_category": posts_by_category,
        "most_used_category": most_used_category,
        "posts_this_month": posts_this_month,
        "category_labels": category_labels,   # ✅ added
        "category_counts": category_counts,   # ✅ added
    }

    return render(request, "reports/posts_dashboard.html", context)