import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    ################################ +++++++++++++++++ ######################################

    def test_addition_int(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_addition_float(self):
        self.assertEqual(self.calculator.addition(3.5, 3.5), 7)

    def test_addition_float_int(self):
        self.assertEqual(self.calculator.addition(3.5, 3), 6.5)

    def test_addition_negative(self):
        self.assertEqual(self.calculator.addition(-15, -25), -40)

    def test_addition_negative_positive(self):
        self.assertEqual(self.calculator.addition(10, -20), -10)

    def test_addition_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.addition, 'z', 33)

    def test_addition_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.addition(None, None)
            self.calculator.addition([], 0)
            self.calculator.addition("aaaaaaaa", "uuuuuuuu")
            self.calculator.addition([123, 321], {"aaaaaa": 123})
            self.calculator.addition({"aaaaaa": 123}, [123, 321])
            self.calculator.addition(None, "aaaaaa")
            self.calculator.addition("aaaaaa", None)
            self.calculator.addition("aaaaa", 777)
            self.calculator.addition(777, "aaaaaaaa")

    def test_add_inf(self):
        self.assertEqual(self.calculator.addition(math.inf, 777), math.inf)
        self.assertEqual(self.calculator.addition(-math.inf, 777), -math.inf)
        self.assertEqual(self.calculator.multiplication(math.inf, -math.inf), -math.inf)

    def test_add_e(self):
        self.assertEqual(self.calculator.addition(math.e, 777), 779.718281828459)
        self.assertEqual(self.calculator.addition(math.e, math.e), 5.43656365691809)


    ################################ ******************** ######################################

    def test_multiplication_int(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_multiplication_float(self):
        self.assertEqual(self.calculator.multiplication(3.5, 3.5), 12.25)

    def test_multiplication_float_int(self):
        self.assertEqual(self.calculator.multiplication(3.5, 3), 10.5)

    def test_multiplication_zero_int(self):
        self.assertEqual(self.calculator.multiplication(0, 3), 0)

    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiplication(-15, -25), 375)

    def test_multiplication_negative_positive(self):
        self.assertEqual(self.calculator.multiplication(10, -20), -200)

    def test_multiplication_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 'z', 'y')

    def test_multiplication_non_numeric_and_numeric(self):
        self.assertEqual(self.calculator.multiplication('1', 5), '11111')
        self.assertEqual(self.calculator.multiplication('yes', 2), 'yesyes')
        self.assertEqual(self.calculator.multiplication(5, '1'), '11111')
        self.assertEqual(self.calculator.multiplication(2, 'yes'), 'yesyes')
        self.assertEqual(self.calculator.multiplication(-2, 'yes'), '')
        self.assertEqual(self.calculator.multiplication('yes', -2), '')
        self.assertEqual(self.calculator.multiplication('yes', 0), '')
        self.assertEqual(self.calculator.multiplication(0, 'yes'), '')
        self.assertRaises(TypeError, self.calculator.multiplication, 'yes', 2.5)
        self.assertRaises(TypeError, self.calculator.multiplication, 2.5, 'yes')

    def test_multiplication_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication(None, None)
            self.calculator.multiplication([], 0)
            self.calculator.multiplication("aaaaaaaa", "uuuuuuuu")
            self.calculator.multiplication([123, 321], {"aaaaaa": 123})
            self.calculator.multiplication({"aaaaaa": 123}, [123, 321])
            self.calculator.multiplication(None, "aaaaaa")
            self.calculator.multiplication("aaaaaa", None)
            self.calculator.multiplication("aaaaa", 777)
            self.calculator.multiplication(777, "aaaaaaaa")

    def test_multiplication_inf(self):
        self.assertEqual(self.calculator.multiplication(math.inf, 777), math.inf)
        self.assertEqual(self.calculator.multiplication(-math.inf, 777), -math.inf)
        self.assertEqual(self.calculator.multiplication(math.inf, -math.inf), -math.inf)

    def test_multiplication_e(self):
        self.assertEqual(self.calculator.multiplication(math.e, 777),  2112.104980712678)
        self.assertEqual(self.calculator.multiplication(math.e, math.e),  7.3890560989306495)

    ################################ --------------------- ######################################

    def test_subtraction_int(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)

    def test_subtraction_float(self):
        self.assertEqual(self.calculator.subtraction(3.5, 3.5), 0)

    def test_subtraction_float_int(self):
        self.assertEqual(self.calculator.subtraction(3.5, 3), 0.5)

    def test_subtraction_negative(self):
        self.assertEqual(self.calculator.subtraction(-15, -25), 10)

    def test_subtraction_negative_positive(self):
        self.assertEqual(self.calculator.subtraction(10, -20), 30)

    def test_subtraction_periodic(self):
        self.assertEqual(self.calculator.subtraction(1/3, 1/3), 0)
        self.assertEqual(self.calculator.subtraction(1/3, 0.3), 0.033333333333333326)
        self.assertEqual(self.calculator.subtraction(1/3, 0.33333333333), 3.33333360913457e-12)

    def test_subtraction_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 'z', 'x')

    def test_subtraction_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction(None, None)
            self.calculator.subtraction([], 0)
            self.calculator.subtraction("aaaaaaaa", "uuuuuuuu")
            self.calculator.subtraction([123, 321], {"aaaaaa": 123})
            self.calculator.subtraction({"aaaaaa": 123}, [123, 321])
            self.calculator.subtraction(None, "aaaaaa")
            self.calculator.subtraction("aaaaaa", None)
            self.calculator.subtraction("aaaaa", 777)
            self.calculator.subtraction(777, "aaaaaaaa")

    def test_subtraction_inf(self):
        self.assertEqual(self.calculator.subtraction(math.inf, 777), math.inf)
        self.assertEqual(self.calculator.subtraction(-math.inf, 777), -math.inf)
        self.assertEqual(self.calculator.subtraction(math.inf, -math.inf), math.inf)

    def test_subtraction_e(self):
        self.assertEqual(self.calculator.subtraction(math.e, 777),  -774.281718171541)
        self.assertEqual(self.calculator.subtraction(math.e, math.e),   0.0)

    ################################ ///////////////////// ######################################

    def test_division_int(self):
        self.assertEqual(self.calculator.division(10, 2), 5)

    def test_division_float_float(self):
        self.assertEqual(self.calculator.division(2.5, 0.5), 5)

    def test_division_float_int(self):
        self.assertEqual(self.calculator.division(10.5, 3), 3.5)

    def test_division_zero(self):
        self.assertEqual(self.calculator.division(1, 0), None)
        self.assertEqual(self.calculator.division(0, 1), 0)

    def test_division_periodic(self):
        self.assertEqual(self.calculator.division(1, 3), 0.3333333333333333)

    def test_division_negative_negative(self):
        self.assertEqual(self.calculator.division(-10, -5), 2)

    def test_division_negative_positive(self):
        self.assertEqual(self.calculator.division(-10, 5), -2)

    def test_division_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.division, 'z', 'y')

    def test_division_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.division(None, None)
            self.calculator.division([], 0)
            self.calculator.division("aaaaaaaa", "uuuuuuuu")
            self.calculator.division([123, 321], {"aaaaaa": 123})
            self.calculator.division({"aaaaaa": 123}, [123, 321])
            self.calculator.division(None, "aaaaaa")
            self.calculator.division("aaaaaa", None)
            self.calculator.division("aaaaa", 777)
            self.calculator.division(777, "aaaaaaaa")

    def test_division_inf(self):
        self.assertEqual(self.calculator.division(math.inf, 777), math.inf)
        self.assertEqual(self.calculator.division(-math.inf, 777), -math.inf)

    def test_division_e(self):
        self.assertEqual(self.calculator.division(math.e, 777),  0.0034984322116590025)
        self.assertEqual(self.calculator.division(math.e, math.e),  1.0)

    ################################ |abs| ######################################

    def test_absolute_int(self):
        self.assertEqual(self.calculator.absolute(5), 5)

    def test_absolute_float(self):
        self.assertEqual(self.calculator.absolute(5.5), 5.5)

    def test_absolute_negative(self):
        self.assertEqual(self.calculator.absolute(-10), 10)

    def test_absolute_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.absolute, 'z')

    def test_absolute_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.absolute(None)
            self.calculator.absolute([])
            self.calculator.absolute("aaaaaaaa")
            self.calculator.absolute([123, 321])
            self.calculator.absolute({"aaaaaa": 123})

    def test_absolute_inf(self):
        self.assertEqual(self.calculator.absolute(math.inf), math.inf)
        self.assertEqual(self.calculator.absolute(-math.inf), math.inf)

    def test_absolute_e(self):
        self.assertEqual(self.calculator.absolute(math.e), math.e)


    ################################ degree ######################################

    def test_degree_int(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree_float_float(self):
        self.assertEqual(self.calculator.degree(0.25, 0.5), 0.5)

    def test_degree_float_int(self):
        self.assertEqual(self.calculator.degree(4, 0.5), 2)

    def test_degree_zero_degree(self):
        self.assertEqual(self.calculator.degree(10, 0), 1)

    def test_degree_negative_base_even(self):
        self.assertEqual(self.calculator.degree(-4, 2), 16)

    def test_degree_negative_base_uneven(self):
        self.assertEqual(self.calculator.degree(-4, 3), -64)

    def test_degree_negative_degree_even(self):
        self.assertEqual(self.calculator.degree(10, -4), 0.0001)

    def test_degree_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.degree, 'z', 'x')

    def test_degree_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.degree(None, None)
            self.calculator.degree([], 0)
            self.calculator.degree("aaaaaaaa", "uuuuuuuu")
            self.calculator.degree([123, 321], {"aaaaaa": 123})
            self.calculator.degree({"aaaaaa": 123}, [123, 321])
            self.calculator.degree(None, "aaaaaa")
            self.calculator.degree("aaaaaa", None)
            self.calculator.degree("aaaaa", 777)
            self.calculator.degree(777, "aaaaaaaa")

    def test_degree_inf(self):
        self.assertEqual(self.calculator.degree(math.inf, 777), math.inf)
        self.assertEqual(self.calculator.degree(-math.inf, 777), -math.inf)
        self.assertEqual(self.calculator.degree(math.inf, -math.inf), 0.0)

    def test_degree_e(self):
        self.assertRaises(OverflowError, self.calculator.degree, math.e, 777)
        self.assertEqual(self.calculator.degree(math.e, math.e),  15.154262241479259)

    ################################ ln ######################################

    def test_ln_int(self):
        self.assertAlmostEqual(self.calculator.ln(2), 0.6931471805599453)

    def test_ln_float_more_than_1(self):
        self.assertAlmostEqual(self.calculator.ln(2.5), 0.91629073187)

    def test_ln_float_less_than_1(self):
        self.assertAlmostEqual(self.calculator.ln(0.1), (-2.30258509299))

    def test_ln_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)

    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    def test_ln_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.ln, 'z')

    def test_ln_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.ln(None)
            self.calculator.ln([])
            self.calculator.ln("aaaaaaaa")
            self.calculator.ln([123, 321])
            self.calculator.ln({"aaaaaa": 123})

    def test_ln_inf(self):
        self.assertEqual(self.calculator.ln(math.inf), math.inf)
        self.assertRaises(ValueError, self.calculator.ln, -math.inf)

    def test_ln_e(self):
        self.assertEqual(self.calculator.ln(math.e),  1.0)

    ################################ log ######################################

    def test_log_int(self):
        self.assertAlmostEqual(self.calculator.log(16, 2), 4)

    def test_log_float_float(self):
        self.assertAlmostEqual(self.calculator.log(1.2, 2.4), 0.2082559308114424)

    def test_log_float_int(self):
        self.assertAlmostEqual(self.calculator.log(5, 2.5), 1.7564707973660298)

    def test_log_zero_body(self):
        self.assertRaises(ValueError, self.calculator.log, 0, 33)

    def test_log_zero_base(self):
        self.assertRaises(ValueError, self.calculator.log, 33, 0)

    def test_log_negative(self):
        self.assertRaises(ValueError, self.calculator.log, -25, 125)

    def test_log_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.log, 'z', 'x')

    def test_log_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.log(None, None)
            self.calculator.log([], 0)
            self.calculator.log("aaaaaaaa", "uuuuuuuu")
            self.calculator.log([123, 321], {"aaaaaa": 123})
            self.calculator.log({"aaaaaa": 123}, [123, 321])
            self.calculator.log(None, "aaaaaa")
            self.calculator.log("aaaaaa", None)
            self.calculator.log("aaaaa", 777)
            self.calculator.log(777, "aaaaaaaa")

    def test_log_inf(self):
        self.assertEqual(self.calculator.log(math.inf, 777), math.inf)
        self.assertRaises(ValueError, self.calculator.log, -math.inf, 777)
        self.assertRaises(ValueError, self.calculator.log, math.inf, -math.inf)

    def test_log_e(self):
        self.assertEqual(self.calculator.log(math.e, 777),  0.15025301818605585)
        self.assertEqual(self.calculator.log(math.e, math.e),  1.0)

    ################################ sqrt ######################################

    def test_sqrt_int(self):
        self.assertAlmostEqual(self.calculator.sqrt(16), 4)

    def test_sqrt_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(2.4), 1.5491933384829668)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_negative(self):
        self.assertAlmostEqual(self.calculator.sqrt(-2), 8.659560562354934e-17+1.4142135623730951j)

    def test_sqrt_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'z')

    def test_sqrt_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt(None)
            self.calculator.sqrt([])
            self.calculator.sqrt("aaaaaaaa")
            self.calculator.sqrt([123, 321])
            self.calculator.sqrt({"aaaaaa": 123})

    def test_sqrt_inf(self):
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)
        self.assertEqual(self.calculator.sqrt(-math.inf), math.inf)

    def test_sqrt_e(self):
        self.assertEqual(self.calculator.sqrt(math.e),  1.6487212707001282)

    ################################ root ######################################

    def test_nth_root_int(self):
        self.assertAlmostEqual(self.calculator.nth_root(64, 3), 4)

    def test_nth_root_float_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(0.75, 0.75), 0.6814202223120523)

    def test_nth_root_int_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(75, 0.75),  316.28724948815585)

    def test_nth_root_zero_base(self):
        self.assertEqual(self.calculator.nth_root(0, 1), 0)

    def test_nth_root_zero_root(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 1, 0)

    def test_nth_root_negative_base(self):
        self.assertAlmostEqual(self.calculator.nth_root(-3, 6), 1.040041911525952+0.6004684775880013j)

    def test_nth_root_negative_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(3, -6), 0.8326831776556043)

    def test_nth_root_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'z', 'x')

    def test_root_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root(None, None)
            self.calculator.nth_root([], 0)
            self.calculator.nth_root("aaaaaaaa", "uuuuuuuu")
            self.calculator.nth_root([123, 321], {"aaaaaa": 123})
            self.calculator.nth_root({"aaaaaa": 123}, [123, 321])
            self.calculator.nth_root(None, "aaaaaa")
            self.calculator.nth_root("aaaaaa", None)
            self.calculator.nth_root("aaaaa", 777)
            self.calculator.nth_root(777, "aaaaaaaa")

    def test_nth_root_inf(self):
        self.assertEqual(self.calculator.nth_root(math.inf, 777), math.inf)
        self.assertEqual(self.calculator.nth_root(-math.inf, 777), math.inf)
        self.assertEqual(self.calculator.nth_root(math.inf, -math.inf), 1.0)

    def test_nth_root_e(self):
        self.assertEqual(self.calculator.nth_root(math.e, 777),  1.0012878298285641)
        self.assertEqual(self.calculator.nth_root(math.e, math.e),  1.444667861009766)


if __name__ == "__main__":
    unittest.main()
