from elife_app.domain.models import DailyEntry
from elife_app.services.wellness_service import WellnessService


def test_low_score_day():
    service = WellnessService()
    entry = DailyEntry(
        date="2026-01-01", sleep=1, stress=5, friends=1,
        water=1, exercise=1, mood=1, work_hours=10,
        hobbies=1, steps=1, meds=1
    )
    score, advice = service.calculate_score(entry)
    assert score == 8
    assert len(advice) > 0


def test_high_score_day():
    service = WellnessService()
    entry = DailyEntry(
        date="2026-01-01", sleep=3, stress=1, friends=3,
        water=3, exercise=3, mood=3, work_hours=8,
        hobbies=3, steps=3, meds=3
    )
    score, advice = service.calculate_score(entry)
    assert score == 27
    assert len(advice) == 0


def test_medium_score_day():
    service = WellnessService()
    entry = DailyEntry(
        date="2026-01-01", sleep=2, stress=3, friends=2,
        water=2, exercise=2, mood=2, work_hours=8,
        hobbies=2, steps=2, meds=2
    )
    score, advice = service.calculate_score(entry)
    assert score == 17
    assert len(advice) == 0
