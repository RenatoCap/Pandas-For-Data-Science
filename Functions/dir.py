def dir(name: str) -> str:
    """
    Get the direction where the Dataset that we want to
    import is located.
    
    Parameters
    ----------
    name : str
        Name of the Dataset that we will import.
        
    Returns
    -------
    str : Direction where the Dataset is located.
    
    Examples
    --------
    >>> direction = dir('Dataset1.csv')
    >>> direction
        './Datasets/Formatos/Dataset1.csv'
    """
    
    return './Datasets/{}'.format(name)