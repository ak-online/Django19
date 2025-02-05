info = ''
    #Users = Buyer.objects.all()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверка на существование пользователя в базе данных
            if Buyer.objects.filter(name=username).exists():
                info = "Ошибка: пользователь уже существует."
            elif password != repeat_password:
                info = "Ошибка: пароли не совпадают."
            elif int(age) < 18:
                info = "Ошибка: возраст должен быть не менее 18 лет."
            else:

                # Создание нового пользователя

                Buyer.objects.create(name=username, balance=500.0, age=age)
                info = f"Приветствуем, {username}!"

    else:
        form = UserRegister()

    context = {'form': form, 'info': info}
