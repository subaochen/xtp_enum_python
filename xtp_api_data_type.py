# /////////////////////////////////////////////////////////////////////////
# ///@author 中泰证券股份有限公司
# ///@file xtp_api_data_type.h
# ///@brief 定义兼容数据基本类型
# // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // /
# ifndef _XTP_API_DATA_TYPE_H_
# define _XTP_API_DATA_TYPE_H_

# pragma pack(8)

# // / 存放版本号的字符串长度
# # define XTP_VERSION_LEN 16
# // / 版本号类型
# typedef
# char
# XTPVersionType[XTP_VERSION_LEN]
# // / 可交易日字符串长度
# # define XTP_TRADING_DAY_LEN 9
# // / 存放证券代码的字符串长度
# # define XTP_TICKER_LEN 16
# // / 存放证券名称的字符串长度
# # define XTP_TICKER_NAME_LEN 64
# // / 本地报单编号的字符串长度
# # define XTP_LOCAL_ORDER_LEN         11
# // / 交易所单号的字符串长度
# # define XTP_ORDER_EXCH_LEN          17
# // / 成交执行编号的字符串长度
# # define XTP_EXEC_ID_LEN             18
# // / 交易所交易员代码字符串长度
# # define XTP_BRANCH_PBU_LEN          7
# // / 用户资金账户的字符串长度
# # define XTP_ACCOUNT_NAME_LEN        16

# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_LOG_LEVEL是日志输出级别类型
# /////////////////////////////////////////////////////////////////////////


class XTP_LOG_LEVEL:
    XTP_LOG_LEVEL_FATAL = 0  # 严重错误级别
    XTP_LOG_LEVEL_ERROR = 1  # 错误级别
    XTP_LOG_LEVEL_WARNING = 2  # 警告级别
    XTP_LOG_LEVEL_INFO = 3  # info级别
    XTP_LOG_LEVEL_DEBUG = 4  # debug级别
    XTP_LOG_LEVEL_TRACE = 5  # trace级别


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_PROTOCOL_TYPE是通讯传输协议方式
# /////////////////////////////////////////////////////////////////////////
class XTP_PROTOCOL_TYPE:
    XTP_PROTOCOL_TCP = 1  # 采用TCP方式传输
    XTP_PROTOCOL_UDP = 2  # 采用UDP方式传输(仅行情接口支持)


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_EXCHANGE_TYPE是交易所类型
# /////////////////////////////////////////////////////////////////////////
class XTP_EXCHANGE_TYPE:
    XTP_EXCHANGE_SH = 1  # 上证
    XTP_EXCHANGE_SZ = 2  # 深证
    XTP_EXCHANGE_UNKNOWN = 3  # 不存在的交易所类型


# //////////////////////////////////////////////////////////////////////////
# ///@brief XTP_MARKET_TYPE市场类型
# //////////////////////////////////////////////////////////////////////////
class XTP_MARKET_TYPE:
    XTP_MKT_INIT = 0  # 初始化值或者未知
    XTP_MKT_SZ_A = 1  # 深圳A股
    XTP_MKT_SH_A = 2  # 上海A股
    XTP_MKT_UNKNOWN = 3  # 未知交易市场类型


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_PRICE_TYPE是价格类型
# /////////////////////////////////////////////////////////////////////////
class XTP_PRICE_TYPE:
    XTP_PRICE_LIMIT = 1  # 限价单-沪 / 深 / 沪期权（除普通股票业务外，其余业务均使用此种类型）
    XTP_PRICE_BEST_OR_CANCEL = 2  # 即时成交剩余转撤销，市价单-深 / 沪期权
    XTP_PRICE_BEST5_OR_LIMIT = 3  # 最优五档即时成交剩余转限价，市价单-沪
    XTP_PRICE_BEST5_OR_CANCEL = 4  # 最优5档即时成交剩余转撤销，市价单-沪深
    XTP_PRICE_ALL_OR_CANCEL = 5  # 全部成交或撤销, 市价单-深 / 沪期权
    XTP_PRICE_FORWARD_BEST = 6  # 本方最优，市价单-深
    XTP_PRICE_REVERSE_BEST_LIMIT = 7  # 对方最优剩余转限价，市价单-深 / 沪期权
    XTP_PRICE_LIMIT_OR_CANCEL = 8  # 期权限价申报FOK
    XTP_PRICE_TYPE_UNKNOWN = 9  # 未知或者无效价格类型


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_SIDE_TYPE是买卖方向类型
# /////////////////////////////////////////////////////////////////////////
class XTP_SIDE_TYPE:
    # ///买（新股申购，ETF买，配股，信用交易中担保品买）
    XTP_SIDE_BUY = 1
    # ///卖（逆回购，ETF卖，信用交易中担保品卖）
    XTP_SIDE_SELL = 2
    # ///申购
    XTP_SIDE_PURCHASE = 7
    # ///赎回
    XTP_SIDE_REDEMPTION = 8
    # ///拆分
    XTP_SIDE_SPLIT = 9
    # ///合并
    XTP_SIDE_MERGE = 10
    # ///改版之后的side的备兑，暂不支持
    XTP_SIDE_COVER = 11
    # ///改版之后的side锁定（对应开平标识为开）/ 解锁（对应开平标识为平）
    XTP_SIDE_FREEZE = 12
    # // / 融资买入
    XTP_SIDE_MARGIN_TRADE = 21
    # // / 融券卖出
    XTP_SIDE_SHORT_SELL = 22
    # // / 卖券还款
    XTP_SIDE_REPAY_MARGIN = 23
    # // / 买券还券
    XTP_SIDE_REPAY_STOCK = 24
    # // / 现金还款（不放在普通订单协议，另加请求和查询协议）
    XTP_SIDE_CASH_REPAY_MARGIN = 25
    # // / 现券还券
    XTP_SIDE_STOCK_REPAY_STOCK = 26
    # // / 余券划转
    XTP_SIDE_SURSTK_TRANS = 27
    # // / 担保品转入
    XTP_SIDE_GRTSTK_TRANSIN = 28
    # // / 担保品转出
    XTP_SIDE_GRTSTK_TRANSOUT = 29
    # ///未知或者无效买卖方向
    XTP_SIDE_UNKNOWN = 30


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_POSITION_EFFECT_TYPE是开平标识类型
# /////////////////////////////////////////////////////////////////////////
class XTP_POSITION_EFFECT_TYPE:
    # 初始值或未知值开平标识，现货适用
    XTP_POSITION_EFFECT_INIT = 0
    # 开
    XTP_POSITION_EFFECT_OPEN = 1
    # 平
    XTP_POSITION_EFFECT_CLOSE = 2
    # 强平
    XTP_POSITION_EFFECT_FORCECLOSE = 3
    # 平今
    XTP_POSITION_EFFECT_CLOSETODAY = 4
    # 平昨
    XTP_POSITION_EFFECT_CLOSEYESTERDAY = 5
    # 强减
    XTP_POSITION_EFFECT_FORCEOFF = 6
    # 本地强平
    XTP_POSITION_EFFECT_LOCALFORCECLOSE = 7
    # 信用业务追保强平
    XTP_POSITION_EFFECT_CREDIT_FORCE_COVER = 8
    # 信用业务清偿强平
    XTP_POSITION_EFFECT_CREDIT_FORCE_CLEAR = 9
    # 信用业务合约到期强平
    XTP_POSITION_EFFECT_CREDIT_FORCE_DEBT = 10
    # 信用业务无条件强平
    XTP_POSITION_EFFECT_CREDIT_FORCE_UNCOND = 11
    # 未知的开平标识类型
    XTP_POSITION_EFFECT_UNKNOWN = 12


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_ORDER_ACTION_STATUS_TYPE是报单操作状态类型
# /////////////////////////////////////////////////////////////////////////
class XTP_ORDER_ACTION_STATUS_TYPE:
    XTP_ORDER_ACTION_STATUS_SUBMITTED = 1  # 已经提交
    XTP_ORDER_ACTION_STATUS_ACCEPTED = 2  # 已经接受
    XTP_ORDER_ACTION_STATUS_REJECTED = 3  # 已经被拒绝


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_ORDER_STATUS_TYPE是报单状态类型
# /////////////////////////////////////////////////////////////////////////
class XTP_ORDER_STATUS_TYPE:
    XTP_ORDER_STATUS_INIT = 0  # 初始化
    XTP_ORDER_STATUS_ALLTRADED = 1  # 全部成交
    XTP_ORDER_STATUS_PARTTRADEDQUEUEING = 2  # 部分成交
    XTP_ORDER_STATUS_PARTTRADEDNOTQUEUEING = 3  # 部分撤单
    XTP_ORDER_STATUS_NOTRADEQUEUEING = 4  # 未成交
    XTP_ORDER_STATUS_CANCELED = 5  # 已撤单
    XTP_ORDER_STATUS_REJECTED = 6  # 已拒绝
    XTP_ORDER_STATUS_UNKNOWN = 7  # 未知订单状态


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_ORDER_SUBMIT_STATUS_TYPE是报单提交状态类型
# /////////////////////////////////////////////////////////////////////////
class XTP_ORDER_SUBMIT_STATUS_TYPE:
    XTP_ORDER_SUBMIT_STATUS_INSERT_SUBMITTED = 1  # 订单已经提交
    XTP_ORDER_SUBMIT_STATUS_INSERT_ACCEPTED = 2  # 订单已经被接受
    XTP_ORDER_SUBMIT_STATUS_INSERT_REJECTED = 3  # 订单已经被拒绝
    XTP_ORDER_SUBMIT_STATUS_CANCEL_SUBMITTED = 4  # 撤单已经提交
    XTP_ORDER_SUBMIT_STATUS_CANCEL_REJECTED = 5  # 撤单已经被拒绝
    XTP_ORDER_SUBMIT_STATUS_CANCEL_ACCEPTED = 6  # 撤单已经被接受


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_TE_RESUME_TYPE是公有流（订单响应、成交回报）重传方式
# /////////////////////////////////////////////////////////////////////////
class XTP_TE_RESUME_TYPE:
    XTP_TERT_RESTART = 0  # 从本交易日开始重传
    XTP_TERT_RESUME = 1  # 从从上次收到的续传（暂未支持）
    XTP_TERT_QUICK = 2  # 只传送登录后公有流（订单响应、成交回报）的内容


# //////////////////////////////////////////////////////////////////////////
# ///@brief ETF_REPLACE_TYPE现金替代标识定义
# //////////////////////////////////////////////////////////////////////////
class ETF_REPLACE_TYPE:
    ERT_CASH_FORBIDDEN = 0  # 禁止现金替代
    ERT_CASH_OPTIONAL = 1  # 可以现金替代
    ERT_CASH_MUST = 2  # 必须现金替代
    ERT_CASH_RECOMPUTE_INTER_SZ = 3  # 深市退补现金替代
    ERT_CASH_MUST_INTER_SZ = 4  # 深市必须现金替代
    ERT_CASH_RECOMPUTE_INTER_OTHER = 5  # 非沪深市场成分证券退补现金替代
    ERT_CASH_MUST_INTER_OTHER = 6  # 表示非沪深市场成份证券必须现金替代
    EPT_INVALID = 7  # 无效值


# //////////////////////////////////////////////////////////////////////////
# ///@brief XTP_TICKER_TYPE证券类型
# //////////////////////////////////////////////////////////////////////////
class XTP_TICKER_TYPE:
    XTP_TICKER_TYPE_STOCK = 0  # 普通股票
    XTP_TICKER_TYPE_INDEX = 1  # 指数
    XTP_TICKER_TYPE_FUND = 2  # 基金
    XTP_TICKER_TYPE_BOND = 3  # 债券
    XTP_TICKER_TYPE_OPTION = 4  # 期权
    XTP_TICKER_TYPE_TECH_STOCK = 5  # 科创板股票（上海）
    XTP_TICKER_TYPE_UNKNOWN = 6  # 未知类型


# //////////////////////////////////////////////////////////////////////////
# ///@brief XTP_BUSINESS_TYPE证券业务类型
# //////////////////////////////////////////////////////////////////////////
class XTP_BUSINESS_TYPE:
    XTP_BUSINESS_TYPE_CASH = 0  # 普通股票业务（股票买卖，ETF买卖等）
    XTP_BUSINESS_TYPE_IPOS = 1  # 新股申购业务（对应的price type需选择限价类型）
    XTP_BUSINESS_TYPE_REPO = 2  # 回购业务(对应的price type填为限价，side填为卖)
    XTP_BUSINESS_TYPE_ETF = 3  # ETF申赎业务
    XTP_BUSINESS_TYPE_MARGIN = 4  # 融资融券业务（暂未支持）
    XTP_BUSINESS_TYPE_DESIGNATION = 5  # 转托管（未支持）
    XTP_BUSINESS_TYPE_ALLOTMENT = 6  # 配股业务（对应的price type需选择限价类型, side填为买）
    XTP_BUSINESS_TYPE_STRUCTURED_FUND_PURCHASE_REDEMPTION = 7  # 分级基金申赎业务
    XTP_BUSINESS_TYPE_STRUCTURED_FUND_SPLIT_MERGE = 8  # 分级基金拆分合并业务
    XTP_BUSINESS_TYPE_MONEY_FUND = 9  # 货币基金业务（暂未支持）
    XTP_BUSINESS_TYPE_OPTION = 10  # 期权业务
    XTP_BUSINESS_TYPE_EXECUTE = 11  # 行权
    XTP_BUSINESS_TYPE_FREEZE = 12  # 锁定解锁，暂不支持
    XTP_BUSINESS_TYPE_UNKNOWN = 13  # 未知类型


# //////////////////////////////////////////////////////////////////////////
# ///@brief XTP_ACCOUNT_TYPE账户类型
# //////////////////////////////////////////////////////////////////////////
class XTP_ACCOUNT_TYPE:
    XTP_ACCOUNT_NORMAL = 0  # 普通账户
    XTP_ACCOUNT_CREDIT = 1  # 信用账户
    XTP_ACCOUNT_DERIVE = 2  # 衍生品账户

    XTP_ACCOUNT_UNKNOWN = 3  # 未知账户类型


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_FUND_TRANSFER_TYPE是资金流转方向类型
# /////////////////////////////////////////////////////////////////////////
class XTP_FUND_TRANSFER_TYPE:
    XTP_FUND_TRANSFER_OUT = 0  # 转出 从XTP转出到柜台
    XTP_FUND_TRANSFER_IN = 1  # 转入 从柜台转入XTP
    # 跨节点转出 从本XTP节点1，转出到对端XTP节点2，XTP服务器之间划拨，只能跨账户用户使用
    XTP_FUND_INTER_TRANSFER_OUT = 2
    # 跨节点转入 从对端XTP节点2，转入到本XTP节点1，XTP服务器之间划拨，只能跨账户用户使用
    XTP_FUND_INTER_TRANSFER_IN = 3
    XTP_FUND_TRANSFER_UNKNOWN = 4  # 未知类型


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_FUND_OPER_STATUS柜台资金操作结果
# /////////////////////////////////////////////////////////////////////////
class XTP_FUND_OPER_STATUS:
    XTP_FUND_OPER_PROCESSING = 0  # XTP已收到，正在处理中
    XTP_FUND_OPER_SUCCESS = 1  # 成功
    XTP_FUND_OPER_FAILED = 2  # 失败
    XTP_FUND_OPER_SUBMITTED = 3  # 已提交到集中柜台处理
    XTP_FUND_OPER_UNKNOWN = 4  # 未知


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_SPLIT_MERGE_STATUS是一个基金当天拆分合并状态类型
# /////////////////////////////////////////////////////////////////////////
class XTP_SPLIT_MERGE_STATUS:
    XTP_SPLIT_MERGE_STATUS_ALLOW = 0  # 允许拆分和合并
    XTP_SPLIT_MERGE_STATUS_ONLY_SPLIT = 1  # 只允许拆分，不允许合并
    XTP_SPLIT_MERGE_STATUS_ONLY_MERGE = 2  # 只允许合并，不允许拆分
    XTP_SPLIT_MERGE_STATUS_FORBIDDEN = 3  # 不允许拆分合并


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_TBT_TYPE是一个逐笔回报类型
# /////////////////////////////////////////////////////////////////////////
class XTP_TBT_TYPE:
    XTP_TBT_ENTRUST = 1  # 逐笔委托
    XTP_TBT_TRADE = 2  # 逐笔成交


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_OPT_CALL_OR_PUT_TYPE是一个认沽或认购类型
# /////////////////////////////////////////////////////////////////////////
class XTP_OPT_CALL_OR_PUT_TYPE:
    XTP_OPT_CALL = 1  # 认购
    XTP_OPT_PUT = 2  # 认沽


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_OPT_EXERCISE_TYPE_TYPE是一个行权方式类型
# /////////////////////////////////////////////////////////////////////////
class XTP_OPT_EXERCISE_TYPE_TYPE:
    XTP_OPT_EXERCISE_TYPE_EUR = 1  # 欧式
    XTP_OPT_EXERCISE_TYPE_AME = 2  # 美式


# /////////////////////////////////////////////////////////////////////////
# ///@brief XTP_POSITION_DIRECTION_TYPE是一个持仓方向类型
# /////////////////////////////////////////////////////////////////////////
class XTP_POSITION_DIRECTION_TYPE:
    XTP_POSITION_DIRECTION_NET = 0  # 净
    XTP_POSITION_DIRECTION_LONG = 1  # 多（期权则为权利方）
    XTP_POSITION_DIRECTION_SHORT = 2  # 空（期权则为义务方）
    XTP_POSITION_DIRECTION_COVERED = 3  # 备兑（期权则为备兑义务方）


# // ////////////////////////////////////////////////////////////////////// /
# ///@brief XTP_CRD_CASH_REPAY_STATUS是一个融资融券直接还款状态类型
# // ////////////////////////////////////////////////////////////////////// /
class XTP_CRD_CR_STATUS:
    XTP_CRD_CR_INIT = 0  # 初始、未处理状态
    XTP_CRD_CR_SUCCESS = 1  # 已成功处理状态
    XTP_CRD_CR_FAILED = 2  # 处理失败状态


# // ////////////////////////////////////////////////////////////////////// /
# ///TXTPTradeTypeType是成交类型类型
# // ////////////////////////////////////////////////////////////////////// /
class TXTPTradeTypeType:
    # 普通成交
    XTP_TRDT_COMMON = 0
    # 现金替代
    XTP_TRDT_CASH = 1
    # 一级市场成交
    XTP_TRDT_PRIMARY = 2
    # 跨市场资金成交
    XTP_TRDT_CROSS_MKT_CASH = 3


# // ////////////////////////////////////////////////////////////////////// /
# ///TXTPOrderTypeType是报单类型类型
# // ////////////////////////////////////////////////////////////////////// /
class TXTPOrderTypeType:
    # 正常
    XTP_ORDT_Normal = 0
    # 报价衍生
    XTP_ORDT_DeriveFromQuote = 1
    # 组合衍生
    XTP_ORDT_DeriveFromCombination = 2
    # 组合报单
    XTP_ORDT_Combination = 3
    # 条件单
    XTP_ORDT_ConditionalOrder = 4
    # 互换单
    XTP_ORDT_Swap = 5

# pragma pack()

# endif
