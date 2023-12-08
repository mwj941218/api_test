import  unittest


class TsetRecharge(unittest.TestCase):

    """用于修饰类方法（Class Method）。类方法是绑定到类而不是实例的方法，因此可以通过类名直接调用，而不需要先创建实例。
    在类方法内部，可以访问类变量和其他类方法，但不能访问实例变量和实例方法。
    使用@classmethod修饰器可以将一个普通方法转化为类方法。被@classmethod修饰的方法的第一个参数通常被命名为cls，
    它表示调用该方法的类本身，而不是实例。通过cls参数，可以在方法内部访问类变量和其他类方法，并且可以在子类中正确地覆盖该方法。
    """
    @classmethod
    def setUpClass(cls) -> None:
        """
        调用登录接口
        得到ID，token，设置为类属性
        """
        pass
    def test_recharge(self):
        pass
