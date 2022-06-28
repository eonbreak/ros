from setuptools import setup

package_name = 'publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Alper ARIK',
    maintainer_email='alper.arik@savronik.com.tr',
    description='ROS Publisher Example',
    license='SVRN',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'iot_publisher = publisher.iot_publisher:main'
        ],
    },
)
