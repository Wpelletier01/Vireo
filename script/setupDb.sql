-- Script to initiate the database of Vireo


CREATE TABLE Channels (
    ChannelID int(10) unsigned NOT NULL AUTO_INCREMENT,
    Name varchar(25) NOT NULL,
  	Salt varchar(29) NOT NULL UNIQUE,
  	Password varchar(60) NOT NULL UNIQUE,
    PRIMARY KEY (ChannelID)
); 
  
CREATE TABLE ChannelDetails (
    CDetailID int(10) unsigned NOT NULL AUTO_INCREMENT,
    ChannelID int(10) unsigned NOT NULL,
    Fname varchar(25) NOT NULL,
    Mname varchar(25) DEFAULT NULL,
    Lname varchar(25) NOT NULL,
    Email varchar(100) NOT NULL,
    Birth date NOT NULL,
    PRIMARY KEY (CDetailID),
    FOREIGN KEY (ChannelID) REFERENCES Channels(ChannelID)
); 

CREATE TABLE Videos (
    VideoID int(10) unsigned NOT NULL AUTO_INCREMENT,
    PathHash varchar(5) NOT NULL,
    ChannelID int(10) unsigned NOT NULL,
    Title varchar(255) NOT NULL,
    Length int(11) NOT NULL,
    Quality int(6) NOT NULL,
    Description text NOT NULL,
    Upload datetime NOT NULL,
    `Like` int(12) NOT NULL DEFAULT 0,
    Dislike int(12) NOT NULL DEFAULT 0,
    PRIMARY KEY (VideoID),
   	FOREIGN KEY (ChannelID) REFERENCES Channels(ChannelID)
);

CREATE TABLE Comments (
    CommentID int(10) unsigned NOT NULL AUTO_INCREMENT,
    Username varchar(25) NOT NULL,
    VideoID int(10) unsigned NOT NULL,
    Content mediumtext NOT NULL,
    Upload datetime NOT NULL,
    ChannelID int(10) unsigned NOT NULL,
    PRIMARY KEY (CommentID),
    FOREIGN KEY (ChannelID) REFERENCES Channels(ChannelID),
    FOREIGN KEY (VideoID) REFERENCES Videos(VideoID)
);