-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydash
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydash` ;

-- -----------------------------------------------------
-- Schema mydash
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydash` DEFAULT CHARACTER SET utf8 ;
USE `mydash` ;

-- -----------------------------------------------------
-- Table `mydash`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydash`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `profession` VARCHAR(45) NULL DEFAULT 'None',
  `email` VARCHAR(255) NULL,
  `pw` LONGTEXT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydash`.`convos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydash`.`convos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `topic` VARCHAR(255) NULL,
  `convo_starter` LONGTEXT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_convos_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_convos_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydash`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydash`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydash`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `convo_id` INT NOT NULL,
  `comment` LONGTEXT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_comments_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_comments_convos1_idx` (`convo_id` ASC) VISIBLE,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydash`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_comments_convos1`
    FOREIGN KEY (`convo_id`)
    REFERENCES `mydash`.`convos` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydash`.`functions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydash`.`functions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `name` VARCHAR(255) NULL,
  `location` NVARCHAR(255) NULL,
  `date` NVARCHAR(255) NULL,
  `attire` VARCHAR(45) NULL,
  `description` LONGTEXT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_functions_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_functions_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydash`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydash`.`rsvp`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydash`.`rsvp` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `function_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_rsvp_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_rsvp_functions1_idx` (`function_id` ASC) VISIBLE,
  CONSTRAINT `fk_rsvp_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydash`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_rsvp_functions1`
    FOREIGN KEY (`function_id`)
    REFERENCES `mydash`.`functions` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydash`.`projects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydash`.`projects` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `name` VARCHAR(255) NULL,
  `skills` VARCHAR(255) NULL,
  `type` VARCHAR(10) NULL,
  `description` LONGTEXT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_projects_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_projects_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydash`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydash`.`collabs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydash`.`collabs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `project_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_collabs_projects1_idx` (`project_id` ASC) VISIBLE,
  INDEX `fk_collabs_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_collabs_projects1`
    FOREIGN KEY (`project_id`)
    REFERENCES `mydash`.`projects` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_collabs_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydash`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydash`.`inboxes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydash`.`inboxes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_inboxes_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_inboxes_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydash`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydash`.`chatrooms`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydash`.`chatrooms` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `inbox_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_chatrooms_inboxes1_idx` (`inbox_id` ASC) VISIBLE,
  CONSTRAINT `fk_chatrooms_inboxes1`
    FOREIGN KEY (`inbox_id`)
    REFERENCES `mydash`.`inboxes` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydash`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydash`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `chatroom_id` INT NOT NULL,
  `message` LONGTEXT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_messages_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_messages_chatrooms1_idx` (`chatroom_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydash`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_messages_chatrooms1`
    FOREIGN KEY (`chatroom_id`)
    REFERENCES `mydash`.`chatrooms` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydash`.`skills`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydash`.`skills` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `skill` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydash`.`user_skills`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydash`.`user_skills` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `skill_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_skills_has_users_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_skills_has_users_skills1_idx` (`skill_id` ASC) VISIBLE,
  CONSTRAINT `fk_skills_has_users_skills1`
    FOREIGN KEY (`skill_id`)
    REFERENCES `mydash`.`skills` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_skills_has_users_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydash`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydash`.`networks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydash`.`networks` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `users_id` INT NOT NULL,
  `network` VARCHAR(45) NULL,
  `url` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_networks_users1_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_networks_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `mydash`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
