


rule generate_data:
    output:
        directory('src/data/test_data')
    cache:
        True
    script:
        'src/scripts/test_data.py'
