#学习使用 argparse用法
import  argparse

#创建一个解析器
#ArgumentParser 对象包含将命令行解析成 Python 数据类型所需的全部信息
'''
argparse.ArgumentParser(prog=None, usage=None, description=None, 
epilog=None, parents=[], formatter_class=argparse.HelpFormatter, 
prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, 
conflict_handler='error', add_help=True, allow_abbrev=True, exit_on_error=True)
    prog - 程序的名称（默认：sys.argv[0]）
    usage - 描述程序用途的字符串（默认值：从添加到解析器的参数生成）
    description - 在参数帮助文档之前显示的文本（默认值：无）
    epilog - 在参数帮助文档之后显示的文本（默认值：无）
    parents - 一个 ArgumentParser 对象的列表，它们的参数也应包含在内
    formatter_class - 用于自定义帮助文档输出格式的类
    prefix_chars - 可选参数的前缀字符集合（默认值：'-'）
    fromfile_prefix_chars - 当需要从文件中读取其他参数时，用于标识文件名的前缀字符集合（默认值：None）
    argument_default - 参数的全局默认值（默认值： None）
    conflict_handler - 解决冲突选项的策略（通常是不必要的）
    add_help - 为解析器添加一个 -h/--help 选项（默认值： True）
    allow_abbrev - 如果缩写是无歧义的，则允许缩写长选项 （默认值：True）
    exit_on_error - 决定当错误发生时是否让 ArgumentParser 附带错误信息退出。 (默认值: True)
'''
#给一个 ArgumentParser 添加程序参数信息是通过调用 add_argument() 方法完成的。
#通常，这些调用指定 ArgumentParser 如何获取命令行字符串并将其转换为对象。这些信息在 parse_args() 调用时被存储和使用
parser = argparse.ArgumentParser(description="命令行传入一个数字")

'''
add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
定义单个的命令行参数应当如何解析。每个形参都在下面有它自己更多的描述，长话短说有：
    name or flags - 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
    action - 当参数在命令行中出现时使用的动作基本类型。
    nargs - 命令行参数应当消耗的数目。
    const - 被一些 action 和 nargs 选择所需求的常数。
    default - 当参数未在命令行中出现时使用的值。
    type - 命令行参数应当被转换成的类型。
    choices - 可用的参数的容器。
    required - 此命令行选项是否可省略 （仅选项可用）。
    help - 一个此选项作用的简单描述。
    metavar - 在使用方法消息中使用的参数值示例。
    dest - 被添加到 parse_args() 所返回对象上的属性名
'''
#type是要传入的参数的数据类型  help是该参数的提示信息
#parser.add_argument('integers',type=str,help='传入的数字')


#当传入多个参数时
#parser.add_argument('integers',type=str,nargs='+' ,help='传入的数字')
parser.add_argument('integers',type=int,nargs='+' ,help='传入的数字')
'''
ArgumentParser.parse_args(args=None, namespace=None)
将参数字符串转换为对象并将其设为命名空间的属性。 返回带有成员的命名空间。
之前对 add_argument() 的调用决定了哪些对象被创建以及它们如何被赋值。 请参阅 add_argument() 的文档了解详情。
    args - 要解析的字符串列表。 默认值是从 sys.argv 获取。
    namespace - 用于获取属性的对象。 默认值是一个新的空 Namespace 对象。
'''
args = parser.parse_args()
print(args)
#获取传入的数据
print(args.integers)
#可以对春如数字进行求和 数据类型要换为int
print(sum(args.integers))