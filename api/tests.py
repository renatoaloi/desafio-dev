"""Unit tests"""
from api.models import CnabTemplate, TransactionTypeTemplate
from django.test import TestCase

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
