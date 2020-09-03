"""PR08 solution tests."""
import solution

def test_students_study_evening():
    """Test when evening in students_study."""
    for i in range(18, 25):
        time = i
        assert solution.students_study(time, True) is True
        assert solution.students_study(time, False) is True


def test_students_study_morning():
    """Test when morning in students_study."""
    for i in range(5, 18):
        time = i
        assert solution.students_study(time, True) is True
        assert solution.students_study(time, False) is False


def test_students_study_night():
    """Test when night in students_study."""
    for i in range(1, 5):
        time = i
        assert solution.students_study(time, True) is False
        assert solution.students_study(time, False) is False


def test_lottery_jackpot():
    """Test when all three numbers are five in lottery."""
    assert solution.lottery(5, 5, 5) == 10


def test_lottery_win():
    """Test when all three numbers are the same but not five in lottery."""
    for i in range(0, 10):
        num = i
        if num != 5:
            assert solution.lottery(num, num, num) == 5


def test_lottery_small_win():
    """Test when b and c are different from a in lottery."""
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                if a != b and a != c:
                    assert solution.lottery(a, b, c) == 1


def test_lottery_lose():
    """Test when b or c equals a in lottery."""
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                if (a == b or a == c) and b != c:
                    assert solution.lottery(a, b, c) == 0


def test_fruit_order_ordered_is_0():
    """Test when fruits ordered is zero in fruit_order."""
    for a in range(0, 101):
        for b in range(0, 101):
            assert solution.fruit_order(a, b, 0) == 0


def test_fruit_order_is_impossible():
    """Test when impossible to fulfill order in fruit_order."""
    for a in range(0, 21):
        for b in range(0, 21):
            for c in range(0, 51):
                small_baskets, big_baskets, ordered_amount = a, b, c
                while big_baskets > 0 and ordered_amount > 4:
                    big_baskets -= 1
                    ordered_amount -= 5
                while small_baskets > 0 and ordered_amount > 0:
                    small_baskets -= 1
                    ordered_amount -= 1
                if ordered_amount != 0:
                    assert solution.fruit_order(a, b, c) == -1


def test_fruit_order_num_of_small_baskets():
    """Test how many small baskets it takes to fulfill order."""
    for a in range(0, 21):
        for b in range(0, 21):
            for c in range(0, 51):
                small_baskets, big_baskets, ordered_amount, result = a, b, c, 0
                while big_baskets > 0 and ordered_amount > 4:
                    big_baskets -= 1
                    ordered_amount -= 5
                while small_baskets > 0 and ordered_amount > 0:
                    small_baskets -= 1
                    ordered_amount -= 1
                    result += 1
                if ordered_amount == 0:
                    assert solution.fruit_order(a, b, c) == result