exchange_rate = 69.71
day_cost = 20  # euro
trip_lengths = (10, 12, 15)
flight_cost = 50
flight_per_trip = 2
salary = [1000, 1200, 800, 5500]
holiday_cash = 1000
spendings = (
    (5, 3, 1),
    (5, 10, 2),
    (2, 2, 11),
)

trip_cost = day_cost * sum(trip_lengths)
trip_cost += len(trip_lengths) * flight_per_trip * flight_cost
average_salary = sum(salary) / len(salary)

print('Текщий курс евро к рублю: {}'.format(exchange_rate))
print('Средняя зарплата: {:,.2f} \u20ac ({:,.2f} \u20bd)'.
      format(average_salary, average_salary * exchange_rate))
print('Стоимость проживания: {:,.2f} \u20ac ({:,.2f} \u20bd)'.
      format(trip_cost, trip_cost * exchange_rate))
print('Бюджет на отпуски: {:,.2f} \u20ac ({:,.2f} \u20bd)'.
      format(holiday_cash, holiday_cash * exchange_rate))

for counter, trip_length in enumerate(trip_lengths):
    total_spending = 0
    full_total_spending = 0
    for spending in range(3):
        total_spending += spendings[spending][counter]
        full_total_spending += sum(spendings[spending][:counter+1])

    trip_cost = (
        day_cost * trip_length + flight_per_trip * flight_cost +
        total_spending)
    trips_cost = (
        day_cost * sum(trip_lengths[:counter+1]) +
        flight_per_trip * flight_cost * len(trip_lengths[:counter+1]) +
        full_total_spending)

    print('В {}-м отпуске мы потратили дополнительно по:'.format(counter+1),
          '{:,.2f}, {:,.2f} и {:,.2f} \u20ac'.format(
            spendings[0][counter],
            spendings[1][counter],
            spendings[2][counter]),
          '({:,.2f}, {:,.2f} и {:,.2f} \u20bd)'.format(
            spendings[0][counter] * exchange_rate,
            spendings[1][counter] * exchange_rate,
            spendings[2][counter] * exchange_rate),
          'Всего в {}-м отпуске мы потратили дополнительно'.format(
            counter+1),
          '{:,.2f} \u20ac ({:,.2f} \u20bd)'.format(
            total_spending,
            total_spending * exchange_rate))

    print('Затраты на {}-й отпуск:'.format(counter+1),
          '{:,.2f} \u20ac ({:,.2f} \u20bd).'.format(
            trip_cost,
            trip_cost * exchange_rate),
          '\nВсего затрат на отпуски: {:,.2f} \u20ac ({:,.2f} \u20bd).'.format(
            trips_cost,
            trips_cost * exchange_rate,),
          '\nДенег на {}-й отпуск {}хватит!'.format(
            counter+1,
            'не ' if trips_cost > holiday_cash else ''))
