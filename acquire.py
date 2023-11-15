import requests
import json

import pandas as pd
import time


def developer_data_date(cryptos, file_name):
    
    all_dev_data = []

    for crypto in cryptos:

        date = '10-12-2020' 

        # Define the API URL
        url = f'https://api.coingecko.com/api/v3/coins/{crypto}/history?date={date}'

        # Make a GET request to the API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            mkt_data = data.get('market_data', {})
            com_data = data.get('community_data', {})
            dev_data = data.get('developer_data', {})

            historical_data = {
                'name': data.get('name',{}),
                'dev_price': mkt_data.get('current_price', {}).get('usd', 0),
                'dev_mkt_cap': mkt_data.get('market_cap', {}).get('usd', 0),
                'dev_twitter_followers': com_data.get('twitter_followers', 0),
                'dev_reddit_post_48h': com_data.get('reddit_average_posts_48h', 0),
                'dev_reddit_avg_comments_48h': com_data.get('reddit_average_comments_48h', 0),
                'dev_reddit_subs': com_data.get('reddit_subscribers', 0),
                'dev_reddit_accounts_active_48h': com_data.get('reddit_accounts_active_48h', 0),
                'dev_forks': dev_data.get('forks', 0),
                'dev_stars':dev_data.get('stars', 0), 
                'dev_pull_merged': dev_data.get('pull_requests_merged', 0),
                'dev_pull_contributors': dev_data.get('pull_request_contributors', 0),
                }

            all_dev_data.append(historical_data)
            time.sleep(7)  
            
    all_dev_df = pd.DataFrame(all_dev_data)
    all_dev_df.to_csv(file_name, index = False)
    
    
    return all_dev_df


def c19_data_date(cryptos, file_name):
    
    c19_data = []

    for crypto in cryptos:

        date = '13-03-2020' 

        # Define the API URL
        url = f'https://api.coingecko.com/api/v3/coins/{crypto}/history?date={date}'

        # Make a GET request to the API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            mkt_data = data.get('market_data',{})
            com_data = data.get('community_data', {})
            dev_data = data.get('developer_data', {})

            c19 = {
                'name': data.get('name',{}),
                'c19_price': mkt_data.get('current_price', {}).get('usd', 0),
                'c19_mkt_cap': mkt_data.get('market_cap', {}).get('usd', 0),
                'c19_twitter_followers': com_data.get('twitter_followers', 0),
                'c19_reddit_post_48h': com_data.get('reddit_average_posts_48h', 0),
                'c19_reddit_avg_comments': com_data.get('reddit_average_comments_48h', 0),
                'c19_reddit_subs': com_data.get('reddit_subscribers', 0),
                'c19_reddit_accounts_active': com_data.get('reddit_accounts_active_48h', 0),
                'c19_forks': dev_data.get('forks', 0),
                'c19_stars':dev_data.get('stars', 0), 
                'c19_pull_merged': dev_data.get('pull_requests_merged', 0),
                'c19_pull_contributors': dev_data.get('pull_request_contributors', 0),
                }

            c19_data.append(c19)
            time.sleep(7) 
    
    df = pd.DataFrame(c19_data)
    df.to_csv(file_name, index = False)
    
    return df


def current_crypto_data(cryptos, file_name):

    # Create a DataFrame from the dictionary
    crypto_data = []

    for crypto in cryptos:
        # Define the API URL
        url = f'https://api.coingecko.com/api/v3/coins/{crypto}'

        # Make a GET request to the API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Extract nested data
            developer_data = data.get("developer_data", {})
            community_data = data.get("community_data", {})
            market_data = data.get("market_data", {})
            links = data.get("links", {})

            # Create a dictionary with the desired information
            current_crypto_data = {
                "name": data.get("name", ""),
                "symbol": data.get("symbol", ""),
                "categories": ", ".join(data.get("categories", [])),
                "market_cap": market_data.get("market_cap", {}).get("usd", 0),
                "market_cap_ranking": data.get("market_cap_rank", 0),
                "current_price": market_data.get("current_price", {}).get("usd", 0),
                "homepage": links.get("homepage", [""])[0],
                "repos_url": links.get("repos_url", {}).get("github", ""),
                "sentiment_votes_up_percentage": data.get("sentiment_votes_up_percentage", 0),
                "sentiment_votes_down_percentage": data.get("sentiment_votes_down_percentage", 0),
                "watchlist_portfolio_users": data.get("watchlist_portfolio_users", 0),
                "coingecko_rank": data.get('coingecko_rank', 0),
                "coingecko_score": data.get("coingecko_score", 0),
                "developer_score": data.get("developer_score", 0),
                "community_score": data.get("community_score", 0),
                "liquidity_score": data.get("liquidity_score", 0),
                "public_interest_score": data.get("public_interest_score", 0),
                "ath_price": market_data.get("ath", {}).get("usd", 0),
                "ath_date": market_data.get("ath_date", {}).get("usd", ""),
                "atl_price": market_data.get("atl", {}).get("usd", 0),
                "atl_date": market_data.get("atl_date", {}).get("usd", ""),
                "price_change_24h": market_data.get("price_change_percentage_24h", 0),
                "price_change_7d": market_data.get("price_change_percentage_7d", 0),
                "price_change_30d": market_data.get("price_change_percentage_30d", 0),
                "price_change_60d": market_data.get("price_change_percentage_60d", 0),
                "price_change_1y": market_data.get("price_change_percentage_1y", 0),
                "total_supply": market_data.get("total_supply", 0),
                "max_supply": market_data.get("max_supply", 0),
                "circulating_supply": market_data.get("circulating_supply", 0),
                "last_updated": data.get("last_updated", ""),
                "twitter_followers": community_data.get("twitter_followers", 0),
                "telegram_channel_users": community_data.get("telegram_channel_user_count", 0),
                "forks": developer_data.get("forks", 0),
                "stars": developer_data.get("stars", 0),
                "pull_requests_merged": developer_data.get("pull_requests_merged", 0),
                "contributors": developer_data.get("pull_request_contributors", 0),
                "commit_count_4_weeks": developer_data.get("commit_count_4_weeks", 0)
            }


            crypto_data.append(current_crypto_data)
            time.sleep(5)
            
    df = pd.DataFrame(crypto_data)
    crypto_data.to_csv(file_name, index = False)
    
    return df

