-- MySQL Script generated by MySQL Workbench
-- Thu Jun  6 11:41:12 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Usuario` (
  `ID_usuario` VARCHAR(45) NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `correo_electronico` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID_usuario`),
  UNIQUE INDEX `ID_usuario_UNIQUE` (`ID_usuario` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Tarea`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Tarea` (
  `Usuario_ID_usuario` VARCHAR(45) NOT NULL,
  `ID_tarea` VARCHAR(45) NOT NULL,
  `Categoria` VARCHAR(45) NOT NULL,
  `fecha_vencimiento` DATE NOT NULL,
  `prioridad` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(45) NOT NULL,
  `titulo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Usuario_ID_usuario`),
  CONSTRAINT `fk_Tarea_Usuario`
    FOREIGN KEY (`Usuario_ID_usuario`)
    REFERENCES `mydb`.`Usuario` (`ID_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
