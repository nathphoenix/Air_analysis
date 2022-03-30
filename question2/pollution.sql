-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema pollution
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema pollution
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pollution` DEFAULT CHARACTER SET latin1 ;
USE `pollution` ;

-- -----------------------------------------------------
-- Table `pollution`.`station`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution`.`station` (
  `SiteID` INT(11) NOT NULL,
  `Location` VARCHAR(50) NULL DEFAULT NULL,
  `geo_point_2d` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`SiteID`))
ENGINE = MyISAM
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pollution`.`readings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution`.`readings` (
  `readings_ID` INT(11) NOT NULL,
  `Date_Time` DATETIME(6) NOT NULL,
  `NOx` FLOAT NOT NULL,
  `NO2` FLOAT NOT NULL,
  `NO` FLOAT NOT NULL,
  `PM10` FLOAT NOT NULL,
  `NVPM10` FLOAT NOT NULL,
  `VPM10` FLOAT NOT NULL,
  `NVPM25` FLOAT NOT NULL,
  `PM25` FLOAT NOT NULL,
  `VPM25` FLOAT NOT NULL,
  `CO` FLOAT NOT NULL,
  `O3` FLOAT NOT NULL,
  `SO2` FLOAT NOT NULL,
  `Temperature` FLOAT NOT NULL,
  `RH` FLOAT NOT NULL,
  `Air_Pressure` FLOAT NOT NULL,
  `DateStart` DATETIME(6) NOT NULL,
  `DateEnd` DATETIME(6) NOT NULL,
  `Current` VARCHAR(50) NOT NULL,
  `Instrument_Type` VARCHAR(50) NOT NULL,
  `station_SiteID` INT(11) NOT NULL,
  PRIMARY KEY (`readings_ID`),
  INDEX `fk_readings_station_idx` (`station_SiteID` ASC) )
ENGINE = MyISAM
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `pollution`.`schema`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution`.`schema` (
  `measure` BIGINT(20) NOT NULL,
  `desc` VARCHAR(50) NULL DEFAULT NULL,
  `unit` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`measure`))
ENGINE = MyISAM
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
