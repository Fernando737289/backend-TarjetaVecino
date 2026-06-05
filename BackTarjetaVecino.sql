-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Servidor: mysql
-- Tiempo de generación: 23-05-2026 a las 02:38:10
-- Versión del servidor: 8.0.46
-- Versión de PHP: 8.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `BackTarjetaVecino`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auditoria`
--

CREATE TABLE `auditoria` (
  `id_auditoria` int NOT NULL,
  `tabla_afectada` varchar(100) DEFAULT NULL,
  `accion_realizada` varchar(50) DEFAULT NULL,
  `descripcion` text,
  `usuario_accion` varchar(100) DEFAULT NULL,
  `fecha_accion` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `beneficios`
--

CREATE TABLE `beneficios` (
  `id_beneficio` int NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `descripcion` text,
  `tipo_descuento` enum('porcentaje','monto_fijo','2x1') DEFAULT NULL,
  `valor_descuento` decimal(10,2) DEFAULT NULL,
  `stock` int DEFAULT '0',
  `fecha_inicio` date DEFAULT NULL,
  `fecha_vencimiento` date DEFAULT NULL,
  `comercio` varchar(150) DEFAULT NULL,
  `estado` enum('activo','inactivo') DEFAULT 'activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona`
--

CREATE TABLE `persona` (
  `id_persona` int NOT NULL,
  `rut` varchar(12) NOT NULL,
  `nombres` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `numero_direccion` varchar(10) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `estado` enum('activo','inactivo') DEFAULT 'activo',
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `persona`
--

INSERT INTO `persona` (`id_persona`, `rut`, `nombres`, `apellidos`, `direccion`, `numero_direccion`, `telefono`, `email`, `fecha_nacimiento`, `estado`, `fecha_creacion`) VALUES
(4, '21817151-6', 'Fernando Manuel', 'Maturana Hidalgo', 'example', '4564', '382794627834', 'ejemplo@gmail.com', '2026-05-22', 'activo', '2026-05-22 03:10:45'),
(5, '20.954.697-3', 'guillermo eduardo', 'gonzalez', 'ejemplo', '5678', '12345657876', 'ejemplo@ejemplo.com', '2026-05-03', 'activo', '2026-05-22 21:45:50');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tarjeta`
--

CREATE TABLE `tarjeta` (
  `id_tarjeta` int NOT NULL,
  `id_persona` int NOT NULL,
  `numero_tarjeta` varchar(50) NOT NULL,
  `codigo_qr` longtext NOT NULL,
  `fecha_emision` date NOT NULL,
  `fecha_vencimiento` date NOT NULL,
  `estado` enum('activa','bloqueada','vencida') DEFAULT 'activa'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tarjeta`
--

INSERT INTO `tarjeta` (`id_tarjeta`, `id_persona`, `numero_tarjeta`, `codigo_qr`, `fecha_emision`, `fecha_vencimiento`, `estado`) VALUES
(2, 4, '797161', 'iVBORw0KGgoAAAANSUhEUgAAAcIAAAHCAQAAAABUY/ToAAADi0lEQVR4nO2cXYrrSAxGj8aGfrRhFpCl2DuYJQ29M3spvYCB8mNDGc1DqfyT9GXgktCdzKeHELtyqBiE9ElVZXN+z+Y/fhMEkSJFihQpUqTIn0daWAuzmcVHD8zWYmYtNi71V+M3/1uRP4vE3d0Z3N09Ne7uGQbP+ERTBk6j9XJ6rucU+XhyqfFlthaflje3vxOUYLRZCVX3mlPka5LFc2A15kvGp6WNy8fNKfK5yfb2VpMNwFkM6P4xoLltIz3Xc4p8PNm5+wT4e09IIWiKCirCegSKWrrXnCJfipzNzKyPXFY+RsDGpYUhAbCWsuxec4p8EbLksj1T+XzJFCkEGeg+DboMdOd89lzPKfLRpFlPtIZYWhg+an8IYsCn7Xf3mVPkq5ClPxQCqPNNBW2jqXGGtPWREqg/JPIL0kaA4aPF3T/Nxi7jU+dudqkieu5X8/f+bnOKfBUy9ND8V8Lny6c5S4+z/OkMH212AGcBWN4cuoR9378V+ZPJxczGpcVGGmfuV7Ox+4xabexqMBrSqrpM5JUVnQPEKpmn6CcWURT3IFpInYdJD4msVn0opPOh21i8qXhOJu5pzVXkjUVYKf6SYUhNdSnfLFEi0mFAPiTyRNrIalU15yJ7/L22i8x6YvU1Otbf+29F/izyEIdO3/KxNTTVACU9JPILqz5RvWTT1KefRLuoXCuXibwlbaxpzOzyaRGMto2L0JQtaYci7imfU+QjyGMum9jKes/XAyGskzS1yGvbK69IaO4hrAFiqSyd913Lh0QeLTyiCxFdVPMEHGLTUNQSoNpe5K3tTaBDB4gu1+iTto51Uo9R5Je2q2af9rvdMW9FfqPxqPLlQyKPtpdakdWonaKJaA0dPGc3+ZDIahFp0i6d44zivupR5RHRJFIcEnmy3YfCc0pZn6s37fsYy7dGcUjkL8jGfVrefL9k7mvHeu4bN+vPBxWf9DlF3p3krHI2/Uwt5rt8qMYOx+8Vh0SeyMN7P1jMSi57v8SuIeZ+jQMfc699jCKv7dh/rgsZdQMIWzVWG9iDq7YXeW1HTb2t2287PvZTQsV0Nkjkf5NzT2Sw4aMtcjoWPFIduPucIp+avHnvx5B6Y5hyCzS5HgZazcuJ6i5X4rmeU+TjyBs9VO5tymioXaG9NaRcJvIrcnvvR/GXOGq/WryzgdWOJdl95hT5IqTpHeciRYoUKVKkyP85+S991VnDtXCPsQAAAABJRU5ErkJggg==', '2026-05-22', '2027-05-22', 'activa'),
(4, 5, '753619', 'iVBORw0KGgoAAAANSUhEUgAAAcIAAAHCAQAAAABUY/ToAAADfElEQVR4nO2cz23jPBDF36wE5CgBLsCl0B18JX01bQdiKSlgAeoYgMLsYTgk5U0u2QixvG8OhmXzB4nAw3D+kBLF5yz++CQIkCRJkiRJkiRJPh4pxUYgioh/jOg+sPqo2zc/LcnHIqGqqgiqqpoGVdUMBM3QZSq/IaSh/uuDl3PNk+Tx5Or+JcoIXdYXlf8TgHh9kzbaXNVX3ZPkc5Dj3bWENAPAJhrnBME0KOI8fOU9ST49OajIDACriGrazA/J7ch7kjwx6X5oUgAroHEeoPE2ZMGUgHgbFJgSFCvQFyTPNU+Sx5Elpi5W4ucPPnwUY2qSvZkfav5F4zUD8ZqhwJsoVgCY3kT3Xuhs8yR5NGkBUBQRYB2B8CqCOAMi1wzEuYwugdKX3JPks5C2llkZCJMqAK8FLW1IgpWLbEHjWkZyZyahZcrQxS6zq2SqxUf/zRBqiOTOiobgRWhM2RwPQqpeyuXT6YoaIunW1jJbvIJ9K10PW8aKhlonhBoi2VlpgaW2qrlelsk7Z6oZwFT+LePONU+Sx5G9ckxIXTjd4my/DOy5kvzDWhTU8jKUaqNLSq2Nn6GLC4kaIlmt+aESBXlN2kTThUKtYk0Nkeyt5WXFD3nE47WgmqZVrTEeIrmzVh+CRdJ1LWtDanRtRj9Ecmd9TN0ytAR08bOmfjA1RHJvXW6/ALVY3a9bKPEQwHiI5DvWxUNBa3LmGX1plVm5qLU+qCGSnbkfKp7GM7SW9Ku2wJq5PckPybbPAwDkNqkC61giI6wvinjdBdbnnCfJA8i6lrVIOsNKjjXEduW0/gf9EMnO+lTLi4qqXVWoSKqdL2M8RHJvfT0xoYimdFprcpbKxiLu/SD5jnUaqluHOt9klzWjb86IGiLp5nrJ6JsbXZN1Z4EaInlv9VzHoAAUAgzaTkdL0G3U+F+ChAUQTNm+nW2eJI8jTUMumiEjzr9GBbZRwusIxKan9WL//vU9ST4lWWMfYH1Rkdm7r93xxMmXu29/WpIPSfp7P9R2TL+KANhEF2z20iE/ffaid+R3PC3JxybX0SLpch7RS0Pelt3kQ/Lz9yT5VGScN5Gb73sVmQeVGzax0lC8stdB8s7u3/shAKBYL4qQLkBYthHAkCX8vGQJCZ61nWueJI8j333vh580w+5s0H4DCOtDJIsJ33FOkiRJkiRJkvzHyd9o/I1bU5yxUwAAAABJRU5ErkJggg==', '2026-05-22', '2027-05-22', 'activa');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auditoria`
--
ALTER TABLE `auditoria`
  ADD PRIMARY KEY (`id_auditoria`);

--
-- Indices de la tabla `beneficios`
--
ALTER TABLE `beneficios`
  ADD PRIMARY KEY (`id_beneficio`);

--
-- Indices de la tabla `persona`
--
ALTER TABLE `persona`
  ADD PRIMARY KEY (`id_persona`),
  ADD UNIQUE KEY `rut` (`rut`);

--
-- Indices de la tabla `tarjeta`
--
ALTER TABLE `tarjeta`
  ADD PRIMARY KEY (`id_tarjeta`),
  ADD UNIQUE KEY `id_persona` (`id_persona`),
  ADD UNIQUE KEY `numero_tarjeta` (`numero_tarjeta`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auditoria`
--
ALTER TABLE `auditoria`
  MODIFY `id_auditoria` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `beneficios`
--
ALTER TABLE `beneficios`
  MODIFY `id_beneficio` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `persona`
--
ALTER TABLE `persona`
  MODIFY `id_persona` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `tarjeta`
--
ALTER TABLE `tarjeta`
  MODIFY `id_tarjeta` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tarjeta`
--
ALTER TABLE `tarjeta`
  ADD CONSTRAINT `fk_tarjeta_persona` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
