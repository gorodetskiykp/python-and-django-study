def get_flats_info():
  flats = [
    [3189226, 1, 11, "построена"], # price, rooms, min_to_metro, status
    [3500000, 1, 9, "построена"], 
    [3200000, 1, 20, "построена"],
    [3300000, 1, 8, "построена"], 
    [3400000, 1, 20, "построена"], 
    [3400000, 1, 2, "построена"], 
    [2999000, 2, 16, "построена"], 
    [3490000, 1, 4, "построена"], 
    [2999000, 1, 6, "построена"], 
    [2759730, 1, 1, "строится"], 
    [2369234, 1, 10, "строится"]
  ]
  elevators = [
    'да',
    'да',
    'да',
    'да',
    'да',
    'нет',
    'да',
    'нет',
    'нет',
    'да',
    'да',
  ]
  levels = [1,2,3,4,5,1,1,15,6,14,11]
  return zip(flats, elevators, levels)

print('Список уже построенных квартир, расположенных не дальше 15 минут пешком от метро,',
      'на первом этаже либо с лифтом:')
for i, (flat, elevator, level) in enumerate(get_flats_info()):
    if "построена" in flat[3] and flat[2]<=15 and ('да' in elevator or level==1):
        print (("{}. {}, лифт: {}, этаж: {}").format(i, flat, elevator, level))

budget = 0
while True:
    user_input = input("Введите ваш бюджет (чтобы закончить, введите q):\n>>>")
    if user_input == "q":
        break
    else:
        budget = int(user_input)
    user_input = input("Сколько готовы отдавать в месяц? (чтобы закончить, введите q):\n>>>")
    if user_input == "q":
        break
    else:
        monthly = int(user_input)
    some_flats_aviable = False
    for i, flat in enumerate(get_flats_info()):
      if flat[0][0] <= budget:
        some_flats_aviable = True
        print (("{}. {}").format(i, str(flat)))
        years_to_pay = flat[0][0]/monthly/12
        if years_to_pay < 75:
          print (("На эту квартиру нам придется работать {:.3} месяцев или {:.2} лет").
              format(flat[0][0]/monthly, years_to_pay))
        else:
          print ('Столько не живут!')
    if not some_flats_aviable:
      print('С таким бюджетом Москву не покорить!')
