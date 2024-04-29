For each channel in the image:
    Apply LDR global contrast correction
    Obtain 2D histogram of gray level differences
    Increase contrast based on histogram
    Represent differences and transformation in a tree-like structure
    Define difference variable at each layer
    Ignore inter-layer dependencies
    Find difference vectors and solve equations on each layer
    Combine difference vectors to form transformation function
    Apply transformation function to images
    Obtain local and global contrast enhanced LDR images
Combine LDR images for each channel to get final image
Perform color correction