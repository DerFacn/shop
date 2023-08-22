<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=PT+Sans&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="./css/login.css?v=<?php echo rand(); ?>">
    
    <title>Вход</title>
</head>
<body>
    <form id="login-form" action="login.py" method="get">
        <fieldset id="login-fieldset">
            <legend>Вход</legend>
            <label for="email">Почта: </label>
            <input name="email" type="email" placeholder="user2023@gmail.com" 
                patter="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$" required>
            
            <label for="password">Пароль: </label>
            <input name="password" type="password" placeholder="********"  required>

            <button type="submit">Отпарвить</button>
        </fieldset>
    </form>
</body>
</html>