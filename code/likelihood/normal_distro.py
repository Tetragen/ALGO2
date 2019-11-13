import scipy.stats

mean = 3
std_dev = 1

distro = scipy.stats.norm(mean, std_dev)


def pdf_point(point):
    print(f"proba density of point {point} : {distro.pdf(point)}")


pdf_point(3)
pdf_point(2)
pdf_point(3.5)
pdf_point(1)
pdf_point(10)

