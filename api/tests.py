"""Unit tests"""
from django.test import TestCase
from api.models import CnabTemplate, ImportCnabTemplate, \
    ImportTemplate, TransactionTypeTemplate


class TestTemplateModel(TestCase):
    """Tests for template models"""

    def test_create_cnab_template(self):
        """Test creation of CNAB template"""
        CnabTemplate.objects.create(
            description='tipo',
            start=1,
            end=1,
            size=1,
            commentary='Tipo da transação'
        )
        self.assertEqual(CnabTemplate.objects.count(), 1)

    def test_create_transaction_type_template(self):
        """Test creation of transaction type template"""
        TransactionTypeTemplate.objects.create(
            description='Débito',
            operation='in',
            signal='plus'
        )
        self.assertEqual(TransactionTypeTemplate.objects.count(), 1)

    def test_create_import_template(self):
        """Test creation of import template"""
        ImportTemplate.objects.create(
            description='Import Template Test'
        )
        self.assertEqual(ImportTemplate.objects.count(), 1)

    def test_create_campos_cnab_template(self):
        """Test case for create cnab action"""
        cnab_template = CnabTemplate.objects.create(
            description='tipo',
            start=1,
            end=1,
            size=1,
            commentary='Tipo da transação'
        )
        self.assertEqual(CnabTemplate.objects.count(), 1)
        import_template = ImportTemplate.objects.create(
            description='Import Template Test'
        )
        self.assertEqual(ImportTemplate.objects.count(), 1)
        ImportCnabTemplate.objects.create(
            import_template=import_template,
            cnab_template=cnab_template,
            order=2
        )
        self.assertEqual(ImportCnabTemplate.objects.count(), 1)

    def test_create_campos_cnab_template_import2_must_be_fist(self):
        """Test case for create cnab action"""
        cnab_template = CnabTemplate.objects.create(
            description='tipo',
            start=1,
            end=1,
            size=1,
            commentary='Tipo da transação'
        )
        self.assertEqual(CnabTemplate.objects.count(), 1)
        import_template = ImportTemplate.objects.create(
            description='Import Template Test'
        )
        self.assertEqual(ImportTemplate.objects.count(), 1)
        ImportCnabTemplate.objects.create(
            import_template=import_template,
            cnab_template=cnab_template,
            order=2
        )
        cnab_template2 = CnabTemplate.objects.create(
            description='tipo',
            start=1,
            end=1,
            size=1,
            commentary='Tipo da transação'
        )
        ImportCnabTemplate.objects.create(
            import_template=import_template,
            cnab_template=cnab_template2,
            order=1
        )
        cnab_fields = ImportCnabTemplate.objects.filter(
            import_template=import_template
        ).order_by('order')
        self.assertEqual(ImportCnabTemplate.objects.count(), 2)
        self.assertGreater(
            cnab_fields[1].order, cnab_fields[0].order)
