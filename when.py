fun main() {
    val studentGrade = 85

    val result = when (studentGrade) {
        in 90..100 -> "Отлично"
        in 80 until 90 -> "Хорошо"
        in 70 until 80 -> "Удовлетворительно"
        in 0 until 70 -> "Неудовлетворительно"
        else -> "Некорректная оценка"
    }

    println("Студент получил оценку: $result")
}





fun main() {
    val currentTime = 15 // представим, что время в часах

    val timeOfDay = when (currentTime) {
        in 6..11 -> "Утро"
        in 12..16 -> "День"
        in 17..20 -> "Вечер"
        in 21..23, in 0..5 -> "Ночь"
        else -> "Некорректное время"
    }

    println("Сейчас $timeOfDay")
}