/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 80030
 Source Host           : localhost:3306
 Source Schema         : foodcardms

 Target Server Type    : MySQL
 Target Server Version : 80030
 File Encoding         : 65001

 Date: 30/05/2023 08:54:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for card_info
-- ----------------------------
DROP TABLE IF EXISTS `card_info`;
CREATE TABLE `card_info`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `balance` double NOT NULL,
  `cardlock` int NOT NULL,
  `cardId` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ManageSystem_card_cardId_4ae7fc55_fk_ManageSystem_holder_cardId`(`cardId` ASC) USING BTREE,
  CONSTRAINT `card_info_ibfk_1` FOREIGN KEY (`cardId`) REFERENCES `cardholder_info` (`cardId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 26 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of card_info
-- ----------------------------
INSERT INTO `card_info` VALUES (1, 88, 0, 2022031564);
INSERT INTO `card_info` VALUES (3, 123, 0, 2022031563);
INSERT INTO `card_info` VALUES (14, 0, 0, 2022031562);
INSERT INTO `card_info` VALUES (25, 5, 0, 123);

-- ----------------------------
-- Table structure for cardhistory_info
-- ----------------------------
DROP TABLE IF EXISTS `cardhistory_info`;
CREATE TABLE `cardhistory_info`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cardId` int NOT NULL,
  `opear_time` datetime NOT NULL,
  `money` double NOT NULL,
  `operation` int NOT NULL,
  `info` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ManageSystem_history_cardId_e6e78fab_fk_ManageSys`(`cardId` ASC) USING BTREE,
  CONSTRAINT `cardhistory_info_ibfk_1` FOREIGN KEY (`cardId`) REFERENCES `cardholder_info` (`cardId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 77 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cardhistory_info
-- ----------------------------
INSERT INTO `cardhistory_info` VALUES (7, 2022031564, '2022-12-03 00:31:14', 12, 0, '充值方式是：+支付宝');
INSERT INTO `cardhistory_info` VALUES (8, 2022031564, '2022-12-03 00:37:49', 10, 0, '充值方式是：+微信');
INSERT INTO `cardhistory_info` VALUES (9, 2022031564, '2022-12-03 00:41:32', 8, 0, '充值方式是：+微信');
INSERT INTO `cardhistory_info` VALUES (10, 2022031564, '2022-12-03 00:41:43', 70, 0, '充值方式是：+银行卡');
INSERT INTO `cardhistory_info` VALUES (12, 2022031564, '2022-12-03 23:18:36', 30, 0, '充值方式是：微信');
INSERT INTO `cardhistory_info` VALUES (19, 2022031563, '2022-12-04 00:10:45', 122, 0, '充值方式是：微信');
INSERT INTO `cardhistory_info` VALUES (21, 2022031563, '2022-12-04 00:11:11', 1, 0, '充值方式是：微信');
INSERT INTO `cardhistory_info` VALUES (25, 2022031564, '2022-12-05 01:15:56', 1, 0, '充值方式是：微信');
INSERT INTO `cardhistory_info` VALUES (26, 2022031564, '2022-12-05 01:15:58', 2, 0, '充值方式是：微信');
INSERT INTO `cardhistory_info` VALUES (27, 2022031564, '2022-12-05 01:16:00', 3, 0, '充值方式是：微信');
INSERT INTO `cardhistory_info` VALUES (28, 2022031564, '2022-12-05 01:16:14', 4, 0, '充值方式是：微信');
INSERT INTO `cardhistory_info` VALUES (29, 2022031564, '2022-12-05 01:16:46', 5, 0, '充值方式是：微信');
INSERT INTO `cardhistory_info` VALUES (30, 2022031564, '2022-12-05 01:16:48', 6, 0, '充值方式是：微信');
INSERT INTO `cardhistory_info` VALUES (31, 2022031564, '2022-12-05 01:17:05', 7, 0, '充值方式是：微信');
INSERT INTO `cardhistory_info` VALUES (32, 2022031564, '2022-12-05 01:17:09', 8, 0, '充值方式是：微信');
INSERT INTO `cardhistory_info` VALUES (33, 2022031564, '2022-12-05 01:17:11', 9, 0, '充值方式是：微信');
INSERT INTO `cardhistory_info` VALUES (43, 2022031564, '2022-12-13 01:22:35', 10, 0, '充值方式是：微信');
INSERT INTO `cardhistory_info` VALUES (47, 2022031564, '2022-12-14 17:31:07', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (48, 2022031564, '2022-12-14 17:31:09', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (49, 2022031564, '2022-12-14 17:31:10', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (50, 2022031564, '2022-12-14 17:31:11', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (51, 2022031564, '2022-12-14 17:31:12', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (52, 2022031564, '2022-12-14 17:31:13', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (53, 2022031564, '2022-12-14 17:31:32', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (54, 2022031564, '2022-12-14 17:31:33', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (55, 2022031564, '2022-12-14 17:31:34', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (56, 2022031564, '2022-12-14 17:35:56', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (57, 2022031564, '2022-12-14 17:35:58', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (58, 2022031564, '2022-12-14 17:35:59', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (59, 2022031564, '2022-12-14 17:36:00', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (60, 2022031564, '2022-12-14 17:36:01', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (61, 2022031564, '2022-12-14 17:36:02', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (62, 2022031564, '2022-12-14 17:36:03', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (63, 2022031564, '2022-12-14 17:36:04', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (69, 2022031564, '2022-12-16 10:38:24', 123, 0, '充值方式是：微信');
INSERT INTO `cardhistory_info` VALUES (70, 2022031564, '2022-12-16 10:45:10', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (71, 2022031564, '2022-12-16 10:45:14', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (72, 2022031564, '2022-12-16 10:45:21', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (73, 2022031564, '2022-12-16 10:45:23', -10, 1, '模拟消费');
INSERT INTO `cardhistory_info` VALUES (76, 123, '2022-12-16 11:16:53', 15, 0, '充值方式是：微信');
INSERT INTO `cardhistory_info` VALUES (77, 123, '2022-12-16 11:16:58', -10, 1, '模拟消费');

-- ----------------------------
-- Table structure for cardholder_info
-- ----------------------------
DROP TABLE IF EXISTS `cardholder_info`;
CREATE TABLE `cardholder_info`  (
  `cardId` int NOT NULL,
  `sId` int NOT NULL,
  `name` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `gender` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `phoneNum` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `address` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`cardId`) USING BTREE,
  INDEX `sId`(`sId` ASC) USING BTREE,
  CONSTRAINT `sId` FOREIGN KEY (`sId`) REFERENCES `user_info` (`user`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cardholder_info
-- ----------------------------
INSERT INTO `cardholder_info` VALUES (123, 123, 'eeeee', '男', '12312312312', '123');
INSERT INTO `cardholder_info` VALUES (2022031562, 2022031562, 'user', '男', '12345678910', '浙江万里学院');
INSERT INTO `cardholder_info` VALUES (2022031563, 2022031563, 'qqq', '男', '12112312322', '123');
INSERT INTO `cardholder_info` VALUES (2022031564, 2022031564, 'Dosbo123', '男', '13777777788', '浙江万里学院');

-- ----------------------------
-- Table structure for user_info
-- ----------------------------
DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user` int NOT NULL,
  `pwd` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `type` int NOT NULL,
  `cardHolder` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user`(`user` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 71 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_info
-- ----------------------------
INSERT INTO `user_info` VALUES (17, 2022031564, '123', 1, 0);
INSERT INTO `user_info` VALUES (26, 2022031563, '123', 0, 0);
INSERT INTO `user_info` VALUES (53, 2022031562, '123123', 0, 0);
INSERT INTO `user_info` VALUES (70, 123, '123123', 0, 0);

SET FOREIGN_KEY_CHECKS = 1;
