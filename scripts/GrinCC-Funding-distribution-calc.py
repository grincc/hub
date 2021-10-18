"""
Payments will by default be made 90% in BTC and 10% in Grin unless otherwise
requested by the applicant. Payment in both Grin and Bitcoin will be based on
the monthly average value equivalent of the requested amount.

In case an applicant prefers to be paid less than the default 10%, sound
argumentation why this deviation is required are expected.
"""
import argparse
from datetime import datetime

from pycoingecko import CoinGeckoAPI

BTC_PERCENTAGE = 90
GRIN_PERCENTAGE = 10

MONTHS = -1


def month_delta(date: datetime, delta: int):
    m, y = (date.month + delta) % 12, date.year + (
        (date.month) + delta - 1
    ) // 12
    if not m:
        m = 12
    d = min(
        date.day,
        [
            31,
            29 if y % 4 == 0 and (not y % 100 == 0 or y % 400 == 0) else 28,
            31,
            30,
            31,
            30,
            31,
            31,
            30,
            31,
            30,
            31,
        ][m - 1],
    )
    return date.replace(day=d, month=m, year=y)


def calculate_sma(id: str, vs: str, since: datetime, until: datetime):
    """
    The SMA is easy to calculate and is the average stock price over a certain
    period based on a set of parameters. The moving average is calculated by
    adding a stock's prices over a certain period and dividing the sum by the
    total number of periods.
    """

    cg = CoinGeckoAPI()
    prices = cg.get_coin_market_chart_range_by_id(
        id=id,
        vs_currency=vs.lower(),
        from_timestamp=since.timestamp(),
        to_timestamp=until.timestamp(),
    ).get("prices")

    periods = len(prices)
    total = 0
    for price in prices:
        total += price[1]

    return total / periods


def split_funding(request: float):
    btc = request * (BTC_PERCENTAGE / 100)
    grin = request * (GRIN_PERCENTAGE / 100)
    return btc, grin


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate SMA of a cryptocurrency"
    )

    parser.add_argument(
        "Funding", metavar="funding", type=float, help="Funding Request"
    )
    parser.add_argument("VS", metavar="vs", type=str, help="VS Currency")
    parser.add_argument("Date", metavar="date", type=str, help="Date")
    args = parser.parse_args()

    funding = args.Funding
    vs = args.VS
    date_string = args.Date

    until = datetime.strptime(date_string, "%Y-%m-%d %H:%M")
    since = month_delta(until, MONTHS)

    btc_sma = calculate_sma("bitcoin", vs, since, until)
    grin_sma = calculate_sma("grin", vs, since, until)

    p90, p10 = split_funding(funding)

    bitcoins = p90/btc_sma
    grins = p10/grin_sma

    print(f" Date:\t\t{date_string}")
    print(f" Request:\t{funding:,.2f} {vs.upper()}")
    print(f" {BTC_PERCENTAGE}%:\t\t{p90:,.2f} {vs.upper()}")
    print(f" {GRIN_PERCENTAGE}%:\t\t{p10:,.2f} {vs.upper()}")
    print("\n")
    print(f" Bitcoin SMA:\t{btc_sma:,.8f} {vs.upper()}")
    print(f" Grin SMA:\t{grin_sma:,.8f} {vs.upper()}")
    print("\n")
    print(" DONATION")
    print(" ========")
    print(f" {bitcoins:,.8f}\tBTC")
    print(f" {grins:,.8f}\tツ")
    print("\n")
