import requests
import pandas as pd
import time

def get_limit_up_stocks():
    """
    爬取东方财富涨停池数据，返回连板数>=2的股票
    """
    url = "http://push2ex.eastmoney.com/getTopicZTPool"
    params = {
        "ut": "7eea3edcaed734bea9cbfc24409ed989",
        "dpt": "wz.ztzt",
        "Pageindex": 0,
        "pagesize": 200,
        "sort": "lbc:desc", 
        "date": "20251231" # 最近的一个交易日 (2025-12-31 Wednesday)
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "http://quote.eastmoney.com/center/gridlist.html"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if data and isinstance(data, dict):
            result_data = data.get("data")
            if result_data is None:
                print("API返回的 data 字段为 None (可能是当前时间无数据).")
                return None
                
            if "pool" not in result_data:
                print("API返回的数据中缺少 'pool' 字段.")
                return None
                
            pool = result_data["pool"]
            if not pool:
                print("API返回了空的数据池 (pool为空).")
                return None

            # Proceed with 'pool' found
            df = pd.DataFrame(pool)
        else:
            print("API返回数据格式不符合预期")
            return None

    except Exception as e:
        print(f"请求发生错误: {e}")
        return None

    
    # 确保字段存在
    required_cols = ['n', 'c', 'p', 'zdp', 'lbc']
    for col in required_cols:
        if col not in df.columns:
            print(f"警告: 缺少字段 {col}")
            if col == 'lbc': return None # 核心字段缺失无法进行
    
    # 数据类型转换
    df['lbc'] = pd.to_numeric(df['lbc'], errors='coerce')
    df['p'] = pd.to_numeric(df['p'], errors='coerce') 
    # 修正：根据经验，ztpool里的p通常是实际价格，不需要除以1000。
    
    # 过滤 lbc >= 2
    continuous_limit_up = df[df['lbc'] >= 2].copy()
    
    # 如果API没支持sort params，我们手动排序
    continuous_limit_up = continuous_limit_up.sort_values(by='lbc', ascending=False)
    
    # 选择展示列
    columns_map = {
        'c': '代码',
        'n': '名称',
        'p': '最新价',
        'zdp': '涨跌幅(%)',
        'lbc': '连板数',
        'hybk': '行业板块'
    }
    
    cols_to_show = [c for c in columns_map.keys() if c in continuous_limit_up.columns]
    result = continuous_limit_up[cols_to_show].rename(columns=columns_map)
    
    return result.head(10)

if __name__ == "__main__":
    print(f"正在获取东方财富涨停数据...")
    top_10 = get_limit_up_stocks()
    if top_10 is not None and not top_10.empty:
        print(f"\n找到 {len(top_10)} 支符合条件的股票 (展示前10):")
        
        # 简单处理价格显示，如果发现价格都大于1000，可能是单位问题
        if top_10['最新价'].mean() > 500: # 粗略判断
             top_10['最新价'] = top_10['最新价'] / 1000.0
             
        print(top_10.to_string(index=False))
    else:
        print("未找到符合连板条件的股票。")
