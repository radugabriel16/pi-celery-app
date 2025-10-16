from .celery_app import celery
from decimal import Decimal, getcontext, ROUND_FLOOR

@celery.task(bind=True)
def calculate_pi(self, n):
    print(f"Calculating π with {n} decimals")

    getcontext().prec = n + 5

    # Gauss–Legendre
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)

    total_steps = 10
    for step in range(total_steps):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2

        progress = (step + 1) / total_steps

        # Sending constant updates with the progress
        self.update_state(
            state='PROGRESS',
            meta={'progress': round(progress, 2)}
        )

    pi = (a + b) ** 2 / (4 * t)

    fmt = Decimal('1.' + '0' * n)
    pi = pi.quantize(fmt, rounding=ROUND_FLOOR)

    return str(pi)


