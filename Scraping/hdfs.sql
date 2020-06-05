CREATE EXTERNAL TABLE IF NOT EXISTS auction_info(auctionid String, bid String, bidtime FLOAT, bidder String, bidderrate INT, openbid FLOAT, price FLOAT, item String, auction_type String) 
COMMENT 'Auction Datails' 
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
