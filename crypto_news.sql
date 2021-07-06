 SQL Dump
-- version 4.1.14
--
-- Client :  127.0.0.1
-- Généré le :  Mar 06 Juillet 2021 à 15:34
-- Version du serveur :  5.6.17
-- Version de PHP :  5.5.12

--
-- Base de données :  `crypto_news`
--

-- --------------------------------------------------------

--
-- Structure de la table `article`
--

CREATE TABLE IF NOT EXISTS `article` (
  `Id_Article` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `date_article` varchar(30) NOT NULL,
  `Id_pub` int(11) NOT NULL,
  PRIMARY KEY (`Id_Article`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `asset`
--

CREATE TABLE IF NOT EXISTS `asset` (
  `Id_Asset` int(11) NOT NULL AUTO_INCREMENT,
  `Name_Asset` varchar(50) NOT NULL,
  `Symbol` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_Asset`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `asset_article`
--

CREATE TABLE IF NOT EXISTS `asset_article` (
  `Id_Asset` int(11) NOT NULL,
  `Id_Article` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `author`
--

CREATE TABLE IF NOT EXISTS `author` (
  `Id_Author` int(11) NOT NULL AUTO_INCREMENT,
  `Name_Author` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_Author`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `author_article`
--

CREATE TABLE IF NOT EXISTS `author_article` (
  `Id_Author` int(11) NOT NULL,
  `Id_Article` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `daily_asset_info`
--

CREATE TABLE IF NOT EXISTS `daily_asset_info` (
  `Id_Asset` int(11) NOT NULL,
  `Daily_Asset_Date` varchar(50) NOT NULL,
  `Price` double NOT NULL,
  `Market_Cap` double NOT NULL,
  `Rank` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `publisher`
--

CREATE TABLE IF NOT EXISTS `publisher` (
  `Id_pub` int(11) NOT NULL AUTO_INCREMENT,
  `name_pub` varchar(50) NOT NULL,
  `url` varchar(255) NOT NULL,
  PRIMARY KEY (`Id_pub`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
