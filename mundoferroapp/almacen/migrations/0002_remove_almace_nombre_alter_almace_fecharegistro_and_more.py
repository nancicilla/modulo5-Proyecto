# Generated by Django 4.1.1 on 2022-10-07 04:39

import almacen.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='almace',
            name='nombre',
        ),
        migrations.AlterField(
            model_name='almace',
            name='fecharegistro',
            field=models.DateField(verbose_name='Fecha de Compra'),
        ),
        migrations.AlterField(
            model_name='almace',
            name='idproducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.producto', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='almace',
            name='preciounitariocompra',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[almacen.validators.validar_precio], verbose_name='Precio de Compra'),
        ),
        migrations.AlterField(
            model_name='almace',
            name='preciounitarioventa',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[almacen.validators.validar_precio], verbose_name='Precio de Venta'),
        ),
        migrations.AlterField(
            model_name='carritocompra',
            name='idcliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='almacen.cliente', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='idcategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categoria', to='almacen.categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='detallecarritocompra',
            name='idCarritoCompra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrito', to='almacen.carritocompra', verbose_name='Carrito de Compras'),
        ),
        migrations.AlterField(
            model_name='detallecarritocompra',
            name='idProducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle', to='almacen.producto', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='fabricante',
            name='responsable',
            field=models.TextField(verbose_name='Responsable(s)'),
        ),
        migrations.AlterField(
            model_name='fabricante',
            name='telefonos',
            field=models.TextField(verbose_name='Teléfono(s)'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='archivo',
            field=models.ImageField(upload_to='images/', verbose_name='Fotografía'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idcategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_producto', to='almacen.categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idfabricante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fabricante', to='almacen.fabricante', verbose_name='Fabricante'),
        ),
    ]